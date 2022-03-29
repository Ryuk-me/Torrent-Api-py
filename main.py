from typing import Optional
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import uvicorn
from helper.is_site_available import check_if_site_available
import json
import os
import time
from dotenv import load_dotenv
import aioredis
import asyncio
from starlette.requests import Request
from starlette.responses import Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CACHE_EXPIRATION = int(os.getenv('CACHE_EXPIRATION', 180)) if os.getenv(
    'PYTHON_ENV', 'dev') == 'prod' else 30


@app.get("/api/v1/search")
@cache(expire=CACHE_EXPIRATION)
async def call_api(site: str, query: str, limit: Optional[int] = 0, page: Optional[int] = 1):
    site = site.lower()
    query = query.lower()
    all_sites = check_if_site_available(site)
    limit = all_sites[site]['limit'] if limit == 0 or limit > all_sites[site]['limit'] else limit
    if all_sites:
        resp = await all_sites[site]['website']().search(query, page, limit)
        if resp == None:
            return {"error": "website blocked change ip or domain"}
        elif len(resp['data']) > 0:
            return resp
        else:
            return {"error": "no results found"}
    return {"error": "invalid site"}


@app.get("/api/v1/trending")
@cache(expire=CACHE_EXPIRATION)
async def get_trending(site: str, limit: Optional[int] = 0, category: Optional[str] = None, page: Optional[int] = 1):
    site = site.lower()
    all_sites = check_if_site_available(site)
    category = category.lower() if category else None
    limit = all_sites[site]['limit'] if limit == 0 or limit > all_sites[site]['limit'] else limit
    if all_sites:
        if all_sites[site]['trending_available']:
            if category != None and not all_sites[site]["trending_category"]:
                return {"error": "search by trending category not available for {}".format(site)}
            if category != None and category not in all_sites[site]['categories']:
                return {"error": "selected category not available", "available_categories": all_sites[site]['categories']}
            resp = await all_sites[site]['website']().trending(category, page, limit)
            if not resp:
                return {"error": "website blocked change ip or domain"}
            elif len(resp['data']) > 0:
                return resp
            else:
                return {"error": "no results found"}

        else:
            return {'error': "trending search not availabe for {}".format(site)}
    return {"error": "invalid site"}


@app.get("/api/v1/category")
@cache(expire=CACHE_EXPIRATION)
async def get_category(site: str, query: str, category: str, limit: Optional[int] = 0, page: Optional[int] = 1):
    all_sites = check_if_site_available(site)
    site = site.lower()
    query = query.lower()
    category = category.lower()
    limit = all_sites[site]['limit'] if limit == 0 or limit > all_sites[site]['limit'] else limit
    if all_sites:
        if all_sites[site]['search_by_category']:
            if category not in all_sites[site]['categories']:
                return {"error": "selected category not available", "available_categories": all_sites[site]['categories']}

            resp = await all_sites[site]['website']().search_by_category(query, category, page, limit)
            if resp == None:
                return {"error": "website blocked change ip or domain"}
            elif len(resp['data']) > 0:
                return resp
            else:
                return {"error": "no results found"}
        else:
            return {"error": "search by category not available for {}".format(site)}
    return {"error": "invalid site"}


@app.get("/api/v1/recent")
@cache(expire=CACHE_EXPIRATION)
async def get_recent(site: str, limit: Optional[int] = 0, category: Optional[str] = None, page: Optional[int] = 1):
    all_sites = check_if_site_available(site)
    site = site.lower()
    category = category.lower() if category else None
    limit = all_sites[site]['limit'] if limit == 0 or limit > all_sites[site]['limit'] else limit
    if all_sites:
        if all_sites[site]['recent_available']:
            if category != None and not all_sites[site]["recent_category_available"]:
                return {"error": "search by recent category not available for {}".format(site)}
            if category != None and category not in all_sites[site]['categories']:
                return {"error": "selected category not available", "available_categories": all_sites[site]['categories']}
            resp = await all_sites[site]['website']().recent(category, page, limit)
            if not resp:
                return {"error": "website blocked change ip or domain"}
            elif len(resp['data']) > 0:
                return resp
            else:
                return {"error": "no results found"}
        else:
            return {"error": "recent search not available for {}".format(site)}
    else:
        return {"error": "invalid site"}


@app.get("/")
async def home():
    return FileResponse('README.md')


@app.get("/api/v1/all/search")
@cache(expire=CACHE_EXPIRATION)
async def get_search_combo(query: str, limit: Optional[int] = 0):
    start_time = time.time()
    query = query.lower()
    # just getting all_sites dictionary
    all_sites = check_if_site_available('1337x')
    sites_list = list(all_sites.keys())
    tasks = []
    COMBO = {
        'data': []
    }
    total_torrents_overall = 0
    for site in sites_list:
        if site == 'libgen':
            continue
        limit = all_sites[site]['limit'] if limit == 0 or limit > all_sites[site]['limit'] else limit
        tasks.append(asyncio.create_task(
            all_sites[site]['website']().search(query, page=1, limit=limit)))
    results = await asyncio.gather(*tasks)
    for res in results:
        if res and len(res['data']) > 0:
            for torrent in res['data']:
                COMBO['data'].append(torrent)
            total_torrents_overall = total_torrents_overall + res['total']
    COMBO['time'] = time.time() - start_time
    COMBO['total'] = total_torrents_overall
    return COMBO


@app.get("/api/v1/all/trending")
@cache(expire=CACHE_EXPIRATION)
async def get_all_trending(limit: Optional[int] = 0):
    start_time = time.time()
    # just getting all_sites dictionary
    all_sites = check_if_site_available('1337x')
    sites_list = [site for site in all_sites.keys(
    ) if all_sites[site]['trending_available'] and all_sites[site]['website']]
    tasks = []
    COMBO = {
        'data': []
    }
    total_torrents_overall = 0
    for site in sites_list:
        if site == 'libgen':
            continue
        limit = all_sites[site]['limit'] if limit == 0 or limit > all_sites[site]['limit'] else limit
        tasks.append(asyncio.create_task(
            all_sites[site]['website']().trending(category=None, page=1, limit=limit)))
    results = await asyncio.gather(*tasks)
    for res in results:
        if res and len(res['data']) > 0:
            for torrent in res['data']:
                COMBO['data'].append(torrent)
            total_torrents_overall = total_torrents_overall + res['total']
    COMBO['time'] = time.time() - start_time
    COMBO['total'] = total_torrents_overall
    return COMBO


@app.get("/api/v1/all/recent")
@cache(expire=CACHE_EXPIRATION)
async def get_all_recent(limit: Optional[int] = 0):
    start_time = time.time()
    # just getting all_sites dictionary
    all_sites = check_if_site_available('1337x')
    sites_list = [site for site in all_sites.keys(
    ) if all_sites[site]['recent_available'] and all_sites[site]['website']]
    tasks = []
    COMBO = {
        'data': []
    }
    total_torrents_overall = 0
    for site in sites_list:
        if site == 'libgen':
            continue
        limit = all_sites[site]['limit'] if limit == 0 or limit > all_sites[site]['limit'] else limit
        tasks.append(asyncio.create_task(
            all_sites[site]['website']().recent(category=None, page=1, limit=limit)))
    results = await asyncio.gather(*tasks)
    for res in results:
        if res and len(res['data']) > 0:
            for torrent in res['data']:
                COMBO['data'].append(torrent)
            total_torrents_overall = total_torrents_overall + res['total']
    COMBO['time'] = time.time() - start_time
    COMBO['total'] = total_torrents_overall
    return COMBO


@app.on_event("startup")
async def startup():
    PYTHON_ENV = os.getenv('PYTHON_ENV', 'dev')
    if PYTHON_ENV == 'prod':
        HOST = os.getenv('REDIS_URI', 'redis://localhost')
    else:
        HOST = 'redis://localhost'
    redis = aioredis.from_url(
        HOST, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8080")

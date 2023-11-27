from fastapi import APIRouter
from typing import Optional
from helper.is_site_available import check_if_site_available
from fastapi import status
from helper.error_messages import error_handler

router = APIRouter(tags=["Search"])


@router.get("/")
@router.get("")
async def search_for_torrents(
    site: str, query: str, limit: Optional[int] = 0, page: Optional[int] = 1
):
    site = site.lower()
    query = query.lower()
    all_sites = check_if_site_available(site)
    if all_sites:
        limit = (
            all_sites[site]["limit"]
            if limit == 0 or limit > all_sites[site]["limit"]
            else limit
        )

        resp = await all_sites[site]["website"]().search(query, page, limit)
        if resp is None:
            return error_handler(
                status_code=status.HTTP_403_FORBIDDEN,
                json_message={"error": "Website Blocked Change IP or Website Domain."},
            )
        elif len(resp["data"]) > 0:
            return resp
        else:
            return error_handler(
                status_code=status.HTTP_404_NOT_FOUND,
                json_message={"error": "Result not found."},
            )

    return error_handler(
        status_code=status.HTTP_404_NOT_FOUND,
        json_message={"error": "Selected Site Not Available"},
    )

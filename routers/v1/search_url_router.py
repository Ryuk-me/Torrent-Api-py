from fastapi import APIRouter, status
from helper.is_site_available import check_if_site_available
from helper.error_messages import error_handler

router = APIRouter(tags=["Torrent By Url"])


# * Only supports 1337x AS OF NOW
@router.get("/")
@router.get("")
async def get_torrent_from_url(site: str, url: str):
    site = site.lower()
    all_sites = check_if_site_available(site)
    if all_sites:
        resp = await all_sites[site]["website"]().get_torrent_by_url(url)
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

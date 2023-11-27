from fastapi import APIRouter, status
from helper.is_site_available import check_if_site_available
from helper.error_messages import error_handler

router = APIRouter(tags=["Get all sites"])


@router.get("/")
@router.get("")
async def get_all_supported_sites():
    all_sites = check_if_site_available("1337x")
    sites_list = [site for site in all_sites.keys() if all_sites[site]["website"]]
    return error_handler(
        status_code=status.HTTP_200_OK,
        json_message={
            "supported_sites": sites_list,
        },
    )

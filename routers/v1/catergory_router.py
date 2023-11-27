from fastapi import APIRouter
from fastapi import status
from typing import Optional
from helper.is_site_available import check_if_site_available
from helper.error_messages import error_handler

router = APIRouter(tags=["Category Torrents Route"])


@router.get("/")
@router.get("")
async def get_category(
    site: str,
    query: str,
    category: str,
    limit: Optional[int] = 0,
    page: Optional[int] = 1,
):
    all_sites = check_if_site_available(site)
    site = site.lower()
    query = query.lower()
    category = category.lower()
    if all_sites:
        limit = (
            all_sites[site]["limit"]
            if limit == 0 or limit > all_sites[site]["limit"]
            else limit
        )

        if all_sites[site]["search_by_category"]:
            if category not in all_sites[site]["categories"]:
                return error_handler(
                    status_code=status.HTTP_404_NOT_FOUND,
                    json_message={
                        "error": "Selected category not available.",
                        "available_categories": all_sites[site]["categories"],
                    },
                )
            resp = await all_sites[site]["website"]().search_by_category(
                query, category, page, limit
            )
            if resp is None:
                return error_handler(
                    status_code=status.HTTP_403_FORBIDDEN,
                    json_message={
                        "error": "Website Blocked Change IP or Website Domain."
                    },
                )
            elif len(resp["data"]) > 0:
                return resp
            else:
                return error_handler(
                    status_code=status.HTTP_404_NOT_FOUND,
                    json_message={"error": "Result not found."},
                )
        else:
            return error_handler(
                status_code=status.HTTP_404_NOT_FOUND,
                json_message={
                    "error": "Category search not availabe for {}.".format(site)
                },
            )
    return error_handler(
        status_code=status.HTTP_404_NOT_FOUND,
        json_message={"error": "Selected Site Not Available"},
    )

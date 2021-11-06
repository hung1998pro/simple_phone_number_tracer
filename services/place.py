import requests
from django.conf import settings

from simple_phone_number_tracer.settings import API_KEY

import logging

logger = logging.getLogger(__name__)

PLACE_DETAILS_FIELDS = [
    "place_id",
    "formatted_address",
    "name",
    "formatted_phone_number",
]


def get_place_ids(address):
    """Get place id from address"""
    url = settings.PLACE_SEARCH_API
    params = {
        "inputtype": "textquery",
        "input": address,
        "fields": "place_id",
        "key": settings.API_KEY,
    }
    res = requests.get(url=url, params=params, timeout=settings.TIMEOUT)
    if res.status_code != 200:
        logger.error(f"Error has occured when getting place ids! {res.text}")
        raise Exception("Error has occured!")
    res_data = res.json()
    candidates = res_data.get("candidates", [])
    return [candidate.get("place_id") for candidate in candidates]


def get_phone_number_from_place_id(place_id):
    """Get phone number from place id"""
    url = settings.PLACE_DETAILS_API
    params = {
        "fields": ",".join(PLACE_DETAILS_FIELDS),
        "key": settings.API_KEY,
        "place_id": place_id,
    }
    res = requests.get(url=url, params=params, timeout=settings.TIMEOUT)
    if res.status_code != 200:
        logger.error(
            f"Error has occured when getting place details! {res.text}"
        )
        raise Exception("Error has occured!")
    res_data = res.json()
    return res_data.get("result")

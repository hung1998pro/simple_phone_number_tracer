from django.test import TestCase
from .mock_data import PLACE_SEARCH, PLACE_DETAILS, ADDRESS
from unittest.mock import Mock, patch
from requests.exceptions import Timeout


class GetPhoneNumberAPITestCase(TestCase):
    """Get Phone Number API TestCase"""

    def setUp(self):
        self.address = ADDRESS

    @patch(
        "phone_number_tracer.api.get_place_ids",
        Mock(return_value=[(PLACE_SEARCH["candidates"][0]["place_id"])]),
    )
    @patch(
        "phone_number_tracer.api.get_phone_number_from_place_id",
        Mock(return_value=PLACE_DETAILS["result"]),
    )
    def test_get_result_from_address(self):
        expected_result = [PLACE_DETAILS["result"]]
        response = self.client.get("/getphonenumber", {"address": ADDRESS})
        res_data = response.json()
        self.assertListEqual(expected_result, res_data["results"])

    @patch("phone_number_tracer.api.get_place_ids", Mock(side_effect=Timeout))
    def test_call_get_place_ids_time_out(self):
        response = self.client.get("/getphonenumber", {"address": ADDRESS})
        status = response.status_code
        self.assertEqual(status, 400)

    @patch(
        "phone_number_tracer.api.get_place_ids",
        Mock(return_value=[(PLACE_SEARCH["candidates"][0]["place_id"])]),
    )
    @patch(
        "phone_number_tracer.api.get_phone_number_from_place_id",
        Mock(side_effect=Timeout),
    )
    def test_call_get_phone_number_from_place_ids_time_out(self):
        response = self.client.get("/getphonenumber", {"address": ADDRESS})
        status = response.status_code
        self.assertEqual(status, 400)

    def test_empty_address(self):
        response = self.client.get("/getphonenumber")
        status = response.status_code
        self.assertEqual(status, 400)

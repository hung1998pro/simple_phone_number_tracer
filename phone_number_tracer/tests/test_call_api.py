from django.test import TestCase
from .mock_data import PLACE_SEARCH, PLACE_DETAILS, ADDRESS
from unittest.mock import Mock, patch
from services.place import get_place_ids, get_phone_number_from_place_id


class CallAPITestCase(TestCase):
    """Call Google API Test Case"""

    def setUp(self):
        self.address = ADDRESS
        self.place_id = PLACE_SEARCH["candidates"][0]["place_id"]

    @patch("services.place.requests")
    def test_call_place_search_api(self, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = PLACE_SEARCH
        mock_response.status_code = 200
        mock_requests.get.return_value = mock_response
        address = self.address
        result = get_place_ids(address)
        # Assert the place id of the result is correct
        self.assertEqual(result[0], PLACE_SEARCH["candidates"][0]["place_id"])

    @patch("services.place.requests")
    def test_call_place_search_fail_status(self, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Mock Response"
        mock_requests.get.return_value = mock_response

        with self.assertRaises(Exception):
            address = self.address
            get_place_ids(address)

    @patch("services.place.requests")
    def test_call_place_detail_api(self, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = PLACE_DETAILS
        mock_response.status_code = 200
        mock_requests.get.return_value = mock_response
        place_id = self.place_id
        result = get_phone_number_from_place_id(place_id)
        # Assert the place id of the result is correct
        self.assertDictEqual(result, PLACE_DETAILS["result"])

    @patch("services.place.requests")
    def test_call_place_detail_fail_status(self, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Mock Response"
        mock_requests.get.return_value = mock_response
        with self.assertRaises(Exception):
            place_id = self.place_id
            get_place_ids(place_id)

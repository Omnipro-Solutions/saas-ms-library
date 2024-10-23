import unittest
import unittest.mock
from unittest.mock import patch

import requests
from src.api_client import get_location


class TestApiClient(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        ip_address = "8.8.8.8"

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "ipAddress": ip_address,
            "countryName": "United States of America",
            "countryCode": "US",
            "cityName": "Mountain View",
            "regionName": "California",
            "continent": "Americas",
            "language": "English",
        }
        location = get_location(ip_address)
        self.assertEqual(location["ipAddress"], ip_address)
        self.assertEqual(location["countryCode"], "US")
        self.assertEqual(location["cityName"], "Mountain View")
        self.assertEqual(location["regionName"], "California")
        self.assertEqual(location["continent"], "Americas")
        self.assertEqual(location["language"], "English")

        mock_get.assert_called_once_with(f"https://freeipapi.com/api/json/{ip_address}")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        ip_address = "8.8.8.8"
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "ipAddress": ip_address,
                    "countryName": "United States of America",
                    "countryCode": "US",
                    "cityName": "Mountain View",
                    "regionName": "California",
                    "continent": "Americas",
                    "language": "English",
                },
            ),
        ]
        with self.assertRaises(requests.exceptions.RequestException):
            get_location(ip_address)

        location = get_location(ip_address)
        self.assertEqual(location["ipAddress"], ip_address)
        self.assertEqual(location["countryCode"], "US")
        self.assertEqual(location["cityName"], "Mountain View")
        self.assertEqual(location["regionName"], "California")
        self.assertEqual(location["continent"], "Americas")
        self.assertEqual(location["language"], "English")

        mock_get.assert_called_with(f"https://freeipapi.com/api/json/{ip_address}")

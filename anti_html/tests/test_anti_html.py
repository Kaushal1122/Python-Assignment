
from unittest.mock import Mock, patch

import pytest
import requests

from src.anti_html import strip_html


@patch("src.anti_html.requests.get")
def test_strip_html(mock_get):
    response = Mock()
    response.text = "<h1>Hello</h1><p>Welcome to Python.</p>"
    mock_get.return_value = response

    result = strip_html("https://example.com")

    assert result == "Hello\nWelcome to Python."
    mock_get.assert_called_once_with("https://example.com", timeout=10)
    response.raise_for_status.assert_called_once()


@patch("src.anti_html.requests.get")
def test_http_error(mock_get):
    response = Mock()
    response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
    mock_get.return_value = response

    with pytest.raises(requests.HTTPError):
        strip_html("https://example.com/missing")

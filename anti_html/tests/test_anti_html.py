
import runpy
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest
import requests

from src import anti_html


@patch("src.anti_html.requests.get")
def test_strip_html(mock_get):
    response = Mock()
    response.text = "<h1>Hello</h1><p>Welcome to Python.</p>"
    mock_get.return_value = response

    result = anti_html.strip_html("https://example.com")

    assert result == "Hello\nWelcome to Python."
    mock_get.assert_called_once_with(
        "https://example.com",
        timeout=10,
    )
    response.raise_for_status.assert_called_once()


@patch("src.anti_html.requests.get")
def test_strip_html_removes_script_and_style(mock_get):
    response = Mock()
    response.text = """
    <html>
        <body>
            <h1>Hello World</h1>
            <script>console.log("JavaScript")</script>
            <style>body { color: red; }</style>
            <p>Welcome to Python.</p>
            <script>alert("Another script")</script>
            <style>p { color: blue; }</style>
        </body>
    </html>
    """
    mock_get.return_value = response

    result = anti_html.strip_html("https://example.com")

    assert "Hello World" in result
    assert "Welcome to Python." in result
    assert "console.log" not in result
    assert "JavaScript" not in result
    assert "color: red" not in result
    assert "alert" not in result
    assert "color: blue" not in result


@patch("src.anti_html.requests.get")
def test_empty_html(mock_get):
    response = Mock()
    response.text = ""
    mock_get.return_value = response

    result = anti_html.strip_html("https://example.com")

    assert result == ""


@patch("src.anti_html.requests.get")
def test_http_error(mock_get):
    response = Mock()
    response.raise_for_status.side_effect = requests.HTTPError(
        "404 Not Found"
    )
    mock_get.return_value = response

    with pytest.raises(requests.HTTPError):
        anti_html.strip_html("https://example.com/missing")


def test_main_success(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["anti_html.py", "https://example.com"],
    )

    with patch(
        "src.anti_html.strip_html",
        return_value="Hello World",
    ) as mock_strip:
        anti_html.main()

    output = capsys.readouterr()

    assert output.out == "Hello World\n"
    mock_strip.assert_called_once_with("https://example.com")


def test_main_http_error(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["anti_html.py", "https://example.com"],
    )

    with patch(
        "src.anti_html.strip_html",
        side_effect=requests.RequestException("Connection failed"),
    ), pytest.raises(SystemExit) as error:
        anti_html.main()

    assert error.value.code == 2

    output = capsys.readouterr()

    assert "Could not download URL" in output.err
    assert "Connection failed" in output.err


def test_script_entry_point(monkeypatch, capsys):
    script_path = Path(anti_html.__file__)

    monkeypatch.setattr(
        sys,
        "argv",
        ["anti_html.py", "https://example.com"],
    )

    response = Mock()
    response.text = "<h1>Entry Point Test</h1>"

    with patch("requests.get", return_value=response):
        runpy.run_path(
            str(script_path),
            run_name="__main__",
        )

    output = capsys.readouterr()

    assert output.out == "Entry Point Test\n"

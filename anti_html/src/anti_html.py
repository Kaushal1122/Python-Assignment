
import argparse

import requests
from bs4 import BeautifulSoup


def strip_html(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator="\n", strip=True)


def main():
    parser = argparse.ArgumentParser(
        description="Download a webpage and print its text without HTML tags."
    )
    parser.add_argument("url", help="URL of the webpage to process")
    args = parser.parse_args()

    try:
        print(strip_html(args.url))
    except requests.RequestException as error:
        parser.error(f"Could not download URL: {error}")


if __name__ == "__main__":
    main()

import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def analyze(site_url, verbose):
    try:
        response = requests.get(site_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        anchors = soup.find_all('a')
        broken_anchors = []

        for anchor in anchors:
            href = anchor.get('href')
            if href and not href.startswith('#'):
                full_url = urljoin(site_url, href)
                if verbose:
                    print(f"Analyzing {full_url}")
                try:
                    link_response = requests.get(full_url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                    link_response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    if verbose:
                        print(f"Request to {full_url} was unsuccessful. Reason: {e}")
                    broken_anchors.append((full_url, f"Error: {e}"))
                else:
                    if link_response.status_code != 200:
                        broken_anchors.append((full_url, link_response.status_code))
                        if verbose:
                            print(f"Request to {full_url} was unsuccessful. Status: {link_response.status_code}")

        return broken_anchors

    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"


def main():
    if len(sys.argv) > 1:
        site_url = sys.argv[1]
        print(f"Searching for broken URLs in {site_url}")
        verbose = sys.argv[2] == "-verbose"
        print("Verbose mode enabled")
        results = analyze(site_url, verbose)
        if isinstance(results, list):
            if results:
                print(f"Found {len(results)} broken links:")
                for broken_link, status_code in results:
                    print(f"- {broken_link}: {status_code}")
            else:
                print("Great! No broken links found.")
        else:
            print(results)
    else:
        print("You need to provide a site URL as a parameter to run the detection!")


if __name__ == "__main__":
    main()

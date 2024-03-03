import difflib
import requests
import time
import argparse


def get_web_content(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print(f"Error fetching web content: {e}")
        return None


def compare_content(current_content, previous_content):
    if not previous_content:
        return None

    differ = difflib.Differ()
    diff = list(differ.compare(previous_content.splitlines(), current_content.splitlines()))

    return diff


def calculate_change_size(diff):
    added_lines = sum(1 for line in diff if line.startswith('+ '))
    removed_lines = sum(1 for line in diff if line.startswith('- '))

    total_lines = added_lines + removed_lines

    if total_lines == 0:
        return "No changes"
    elif total_lines <= 10:
        return "Minor change"
    elif total_lines <= 50:
        return "Medium change"
    else:
        return "Large change"


def apply_filters(content, filters):
    for f in filters:
        content = '\n'.join(line for line in content.splitlines() if f.lower() not in line.lower())
    return content


def main():
    parser = argparse.ArgumentParser(description="Web Changes Notifier")

    parser.add_argument("url",
                        help="URL of the website to monitor")

    parser.add_argument("-t", "--interval", type=int, default=1440,
                        help="Interval in minutes between checks (default is 1440 minutes - 24 hours)")

    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable debug mode (check every 10 sec)")

    args = parser.parse_args()

    url = args.url
    history = []
    filters = ["time", "advertisement"]
    interval_seconds = args.interval * 60  # Convert minutes to seconds
    debug_interval = 20 if args.debug else interval_seconds  # If debug mode, check every 20 seconds
    interval = debug_interval if args.debug else interval_seconds

    print(f"Monitoring changes on {url}")
    print(f"Checking every {interval} {'seconds' if args.debug else 'minutes'} (Debug mode: {'Enabled' if args.debug else 'Disabled'})")

    while True:
        current_content = get_web_content(url)

        if current_content:
            filtered_content = apply_filters(current_content, filters)

            if not history:
                history.append(filtered_content)
                print("Initial content recorded.")
            else:
                diff = compare_content(filtered_content, history[-1])
                change_size = calculate_change_size(diff)

                if change_size != "No changes":
                    print(f"\nWeb content changes detected: {change_size}")
                else:
                    print("No changes detected.")

                history.append(filtered_content)

        if args.debug:
            print(f"Debug mode: Waiting {debug_interval} seconds for the next check.")
        else:
            print(f"Waiting {args.interval} minutes for the next check.")

        time.sleep(debug_interval)


if __name__ == "__main__":
    main()

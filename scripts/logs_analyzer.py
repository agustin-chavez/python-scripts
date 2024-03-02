import re
import sys


def analyze_logs(logs_file):
    try:
        with open(logs_file, 'r') as file:
            errors = []
            warns = []

            for line in file:
                if re.search(r'\bERROR\b', line, re.IGNORECASE):
                    errors.append(line.strip())
                elif re.search(r'\bWARN\b', line, re.IGNORECASE):
                    warns.append(line.strip())

            print("-------- ERRORS --------")
            for error_line in errors:
                print(error_line)

            print("\n-------- WARNS --------")
            for warn_line in warns:
                print(warn_line)

            print("\n-------- REPORT --------")
            print(f"Found {len(errors)} ERRORS and {len(warns)} WARNS")

    except FileNotFoundError:
        print(f"File not found: {logs_file}")
    except PermissionError:
        print(f"Permission error: Unable to read the file {logs_file}")
    except Exception as e:
        print(f"There was an error processing the logs file: {e}")


def main():
    if len(sys.argv) > 1:
        logs_filename = sys.argv[1]
        print(f"Searching for ERRORS and WARNS in {logs_filename}")
        analyze_logs(logs_filename)
    else:
        print("You need to provide the filename of the logs file to analyze")


if __name__ == "__main__":
    main()

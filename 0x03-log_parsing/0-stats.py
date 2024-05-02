#!/usr/bin/python3
""" log parsing """
import sys


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) == 7 and parts[3].isdigit() and int(parts[3]) in status_codes:
                total_size += int(parts[6])
                status_codes[int(parts[3])] += 1
                line_count += 1

            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

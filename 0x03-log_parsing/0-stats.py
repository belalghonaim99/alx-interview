#!/usr/bin/env python3
"""
Script to read stdin line by line and compute metrics:
- Total file size
- Number of lines by status code
"""

import sys


def print_stats(total_size, status_codes):
    """
    Print the accumulated metrics
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        ip, dash, user, date, method, path, protocol, status, size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[-2], parts[-1]

        if not status.isdigit() or not size.isdigit():
            continue

        status = int(status)
        size = int(size)

        if status in status_codes:
            status_codes[status] += 1

        total_size += size
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)

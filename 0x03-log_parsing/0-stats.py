import sys
import signal

# Initialize counters
total_size = 0
status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}


def print_stats():
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

for i, line in enumerate(sys.stdin, 1):
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]

        total_size += size
        if status_code in status_codes:
            status_codes[status_code] += 1

        if i % 10 == 0:
            print_stats()
    except:
        continue

print_stats()
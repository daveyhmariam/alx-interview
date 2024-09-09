import sys
import signal

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Function to print the statistics."""
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Signal handler for keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract the components of the line
            ip_address = parts[0]
            date = parts[3][1:]
            method = parts[5][1:]
            path = parts[6]
            protocol = parts[7][:-1]
            status_code = int(parts[8])
            file_size = int(parts[9])

            # Check if the line format matches the expected format
            if method == "GET" and path.startswith("/projects/260") and protocol == "HTTP/1.1":
                # Update total file size
                total_file_size += file_size

                # Update status code count if it's a known status code
                if status_code in status_codes:
                    status_codes[status_code] += 1

                # Increment line count and print stats after every 10 lines
                line_count += 1
                if line_count % 10 == 0:
                    print_stats()

        except (IndexError, ValueError):
            # Skip the line if there's an error in parsing
            continue

except KeyboardInterrupt:
    # Handle keyboard interruption and print stats
    print_stats()
    sys.exit(0)

# Print final stats if the script ends normally
print_stats()

#!/usr/bin/python3
"""
Log Parsing Project
"""
import sys

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) == 7:  # Assuming each line has 7 parts
            status_code = int(parts[4])
            file_size = int(parts[5])
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

        if line_count == 10:
            print("Total file size: ", total_file_size)
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")
            line_count = 0

except KeyboardInterrupt:
    print("Interrupted!")
    print("Total file size: ", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

#!/usr/bin/python3
"""
Log Parsing Project
"""
import sys


def compute_metrics(file_size, code_status):
    """
    Compute metrics
    """
    print("File size: {}".format(file_size))
    sorted_codes = sorted(code_status.keys())
    for code in sorted_codes:
        if code_status[code] > 0:
            print("{}: {}".format(code, code_status[code]))


num_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                status_code = line.split()[-2]
                if status_code in num_codes.keys():
                    num_codes[status_code] += 1
                # Grab file size
                file_size = int(line.split()[-1])
                total_file_size += file_size
            except Exception:
                pass
            # print metrics if 10 lines have been read
            count += 1
            if count == 10:
                compute_metrics(total_file_size, num_codes)
                count = 0
    except KeyboardInterrupt:
        compute_metrics(total_file_size, num_codes)
        raise

    compute_metrics(total_file_size, num_codes)

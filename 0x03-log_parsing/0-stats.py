#!/usr/bin/python3
"""This module parses an HTTP request log and prints statistics."""
import re


def extract_input(input_line):
    """Extracts the IP, date, request, status code, and file size from a given"""
    f = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(f[0], f[1], f[2], f[3], f[4])
    resp_match = re.fullmatch(log_format, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, sta_codes_sta):
    """Prints the statistics of the log parsing."""
    print('File size: {:d}'.format(total_file_size), flush=True)
    for sta_code in sorted(sta_codes_sta.keys()):
        num = sta_codes_sta.get(sta_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(sta_code, num), flush=True)


def update_metrics(line, total_file_size, sta_codes_sta):
    """Updates the metrics of the log parsing."""
    li = extract_input(line)
    sta_code = li.get('status_code', '0')
    if sta_code in sta_codes_sta.keys():
        sta_codes_sta[sta_code] += 1
    return total_file_size + li['file_size']


def run():
    """Runs the log parsing."""
    line_nums = 0
    total_files_size = 0
    sta_codes_sta = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_files_size = update_metrics(
                line,
                total_files_size,
                sta_codes_sta,
            )
            line_nums += 1
            if line_nums % 10 == 0:
                print_statistics(total_files_size, sta_codes_sta)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_files_size, sta_codes_sta)


if __name__ == '__main__':
    run()

#!/usr/bin/python3
"""
    0-stats.py
"""
import re


def extract_input(input_line):
    """ Extracts the IP, date, request, status code, and file size from a given"""
    format = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    format_info = {
        'status_code': 0,
        'file_size': 0,
    }
    log = '{}\\-{}{}{}{}\\s*'.format(format[0], format[1], format[2], format[3], format[4])
    respoinse = re.fullmatch(log, input_line)
    if respoinse is not None:
        status_code = respoinse.group('status_code')
        fileSize = int(respoinse.group('file_size'))
        format_info['status_code'] = status_code
        format_info['file_size'] = fileSize
    return format_info


def print_statistics(totalFileSize, codeStats):
    """ Prints the statistics of the log parsing."""
    print('File size: {:d}'.format(totalFileSize), flush=True)
    for status_code in sorted(codeStats.keys()):
        nums = codeStats.get(status_code, 0)
        if nums > 0:
            print('{:s}: {:d}'.format(status_code, nums), flush=True)


def update_metrics(line, total_file, codes_stats):
    """ Updates the metrics of the log parsing.

    Args:
        line (str): The input line to parse.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The current status codes statistics.

    Returns:
        int: The updated total file size.
    """
    lineInfo = extract_input(line)
    status_code = lineInfo.get('status_code', '0')
    if status_code in codes_stats.keys():
        codes_stats[status_code] += 1
    return total_file + lineInfo['file_size']


def run():
    """ Runs the log parsing."""
    line_nums = 0
    totalFileSize = 0
    statusCodesStats = {
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
            totalFileSize = update_metrics(
                line,
                totalFileSize,
                statusCodesStats,
            )
            line_nums += 1
            if line_nums % 10 == 0:
                print_statistics(totalFileSize, statusCodesStats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(totalFileSize, statusCodesStats)


if __name__ == '__main__':
    run()

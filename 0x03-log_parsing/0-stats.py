#!/usr/bin/python3
"""read log file"""


def inp_getter(lines):
    """ get the inp """
    line = lines.split(' ')
    return {
        'status_code': line[-2],
        'file_size': int(line[-1]),
    }


def stats(file_size, status_code):
    """ get the stats """
    print('File size: {:d}'.format(file_size), flush=True)
    for status_code in sorted(status_code.keys()):
        n = status_code.get(status_code, 0)
        if n > 0:
            print('{:s}: {:d}'.format(status_code, n), flush=True)


def main():
    """ main """
    line_n = 0
    file_size_sum = 0
    status_codes_stats = {
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
            line_info = inp_getter(line)
            code = line_info.get('status_code', '0')
            if code in status_codes_stats.keys():
                status_codes_stats[code] += 1
            file_size_sum += line_info['file_size']
            line_n += 1
            if line_n % 10 == 0:
                stats(file_size_sum, status_codes_stats)
    except (KeyboardInterrupt, EOFError, SystemExit):
        stats(file_size_sum, status_codes_stats)


if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

if __name__ == "__main__":
    try:
        import sys

        size = 0
        i = 0

        sc = [200, 301, 400, 401, 403, 404, 405, 500]

        ls = {code: 0 for code in sc}

        for line in sys.stdin:
            parts = line.split()
            size += int(parts[-1])
            status_code = int(parts[-2])
            ls[status_code] += 1

            if i == 9:
                i = 0
                print("File size: {}".format(size))
                for k in sorted(ls):
                    print("{}: {}".format(k, ls[k]))
            else:
                i += 1
    except KeyboardInterrupt:
        print(f"File size: {size}")
        for k in sorted(ls):
            print("{}: {}".format(k, ls[k]))
        raise

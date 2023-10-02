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
        sc.sort()

        ls = []
        for line in sys.stdin:
            love = line.split()
            size += int(love[-1])
            ls.append(int(love[-2]))

            if i == 10:
                i = 1
                print("File size: {}".format(size))
                for k in sc:
                    if k in ls:
                        print("{}: {}".format(k, ls.count(k)))
            else:
                i += 1
    except KeyboardInterrupt:
        print(f"File size: {size}")
        for k in sc:
            if k in ls:
                print("{}: {}".format(k, ls.count(k)))
        raise

#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        rt = fct(*args)
    except Exception as e:
        import sys
        sys.stderr.write("Exception: {}\n".format(e));
        rt = None
    return (rt)

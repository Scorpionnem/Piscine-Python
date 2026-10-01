import sys


def is_int(object: any):
    try:
        int(object)
    except ValueError:
        return (False)


try:
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")
    if (len(sys.argv) == 2) and (is_int(sys.argv[1]) is False):
        raise AssertionError("argument is not an integer")

    if (len(sys.argv) == 2):
        if ((int(sys.argv[1]) & 1) == 0):
            print("Im even")
        elif ((int(sys.argv[1]) & 1) == 1):
            print("Im odd")

except AssertionError as e:
    print("AssertionError:", e)

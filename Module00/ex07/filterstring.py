import sys


def ft_filter(function, list):
    """Return an iterator yielding those items of iterable \
for which function(item)
is true. If function is None, return the items that are true."""
    if function:
        return [item for item in list if function(item)]
    return [item for item in list if item]


def main():
    if len(sys.argv) != 3:
        raise AssertionError("Invalid argument count")
    string: str = sys.argv[1]
    try:
        size: int = int(sys.argv[2])
    except ValueError:
        raise AssertionError("Invalid size argument")

    arr = string.split()
    print(ft_filter(lambda s: len(s) > size, arr))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)

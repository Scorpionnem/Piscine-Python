from ft_filter import ft_filter
import sys


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

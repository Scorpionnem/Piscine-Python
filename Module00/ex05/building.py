import sys
import string


def main():
    """'main' main function for the program."""

    if len(sys.argv) > 2:
        raise AssertionError("invalid argument count")

    if len(sys.argv) == 1:
        str = sys.stdin.read()
    else:
        str = sys.argv[1]

    print("The text contains", len(str), "characters:")
    print(sum(1 for c in str if c.isupper()), "upper letters")
    print(sum(1 for c in str if c.islower()), "lower letters")
    print(sum(1 for c in str if c in string.punctuation), "punctuation marks")
    print(sum(1 for c in str if c.isspace()), "spaces")
    print(sum(1 for c in str if c.isdigit()), "digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    pattern = r" ?\b[uU]m\??[,.]?\b"
    match = re.findall(pattern, s)
    num = len(match)
    return num





if __name__ == "__main__":
    main()

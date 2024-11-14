#!/usr/bin/env python3
"""encode binary to b85 txt file"""

from base64 import b85encode


#
def main():
    """main func"""
    infile = input("in:")
    outfile = input("out:")
    with open(infile, "rb") as fr:
        data = fr.read()
        b85data = b85encode(data).decode("utf-8")
    with open(outfile, "w", encoding='utf-8') as fp:
        for i in range(0, len(b85data), 120):
            fp.write(b85data[i : i + 120])
            fp.write("\n")


#
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""decode b85 txt file to binary"""

from base64 import b85decode


#
def main():
    """main func"""
    infile = input("in:")
    outfile = input("out:")
    with open(infile, "rb") as fr:
        data = fr.read()

    with open(outfile, "wb") as fp:
        fp.write(b85decode(data.translate(None, b"\r\n")))


#
if __name__ == "__main__":
    main()

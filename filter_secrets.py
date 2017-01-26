#! /usr/bin/env python

from panflute import *

def filter_secret(elem, doc):
    if isinstance(elem, Div):
        if "secret" in elem.classes:
            return []



if __name__ == "__main__":
    toJSONFilter(filter_secret)

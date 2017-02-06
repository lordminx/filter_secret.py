#! /usr/bin/env python

import os

from panflute import *


def filter_secret(elem, doc):
    if isinstance(elem, Div):
        if get_tag() in elem.classes:
            return []


def get_tag():
    filename = os.path.basename(__file__)
    tag = filename.split("_")[1].split(".")[0]
    return tag




if __name__ == "__main__":
    toJSONFilter(filter_secret)

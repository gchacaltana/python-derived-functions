# !/usr/bin/env python
# -*- coding: utf-8 -*-

HYPHEN_LEN = 70
COLOR_YELLOW = "\033[93m"
END_COLOR = "\033[0m"
COLOR_GREEN = "\033[92m"


def printHyphen():
    print('\n'.ljust(HYPHEN_LEN, '-'))


def highlight(message: str):
    print("\n{}\n".format(COLOR_YELLOW + message + END_COLOR))


def labelInput(message: str):
    return COLOR_GREEN + message + END_COLOR

#!/usr/bin/env python

"""
Author   : avi.mehenwal
FileName : argparser_demo.py
Created  : Mon Jan 11 18:37:15 IST 2016

Demonstrates argparser usage with python 3.4
"""

import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-v", help="verbose mode")
parser.add_argument("-a", help="a mode")
parser.add_argument("-b", help="b verbose mode")
parser.add_argument("-c", help="c verbose mode")
parser.add_argument("-d", help="d verbose mode")
parser.add_argument("-e", help="e verbose mode")

args = parser.parse_args()
print(args)
print(type(args))
print(args.a)


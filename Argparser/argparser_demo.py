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

args = parser.parse_args()
print(args)

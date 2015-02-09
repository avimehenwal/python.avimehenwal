#!/usr/bin/env python

# PURPOSE   : Generate a Big file
# AUTHOR    : avimehenwal
# DATE      : 06-Jan-2015


fileHandler = open('big_file.txt', 'w')

for i in range(1000):
    # values to be written in file should be string type TypeError
    fileHandler.write(str(i)+'\n')

fileHandler.close()


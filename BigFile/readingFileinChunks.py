#!/usr/bin/env python

# PURPOSE   : Read a big file in chunks
# AUTHOR    : avimehenwal
# DATE      : 06-jan-2015

BUF_SIZE = 50
fileHandler = open('big_file.txt', 'r')

# specify the chunksize to read from file as argument to (read / readlines) method
# tmp_lines = fileHandler.readlines(BUF_SIZE)
tmp_lines = fileHandler.read(BUF_SIZE)
while tmp_lines:
    # print([line for line in tmp_lines])
    print("Next Chunk")
    print(tmp_lines)
    tmp_lines = fileHandler.read(BUF_SIZE)




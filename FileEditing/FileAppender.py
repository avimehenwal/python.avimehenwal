import re
import os

file open('F:\Avi_OpenSource_CoadingPractise\PYTHON\FileEditing\pom.xml', "r+", encoding = "utf-8")
file.seek(0, os.SEEK_END)
print(file.tell())
pos = file.tell() - 1
print(pos)
while pos > 0 and file.read(1) != "\n":
    pos -= 1
    file.seek(pos, os.SEEK_SET)
if pos > 0:
    print(pos)
    file.seek(pos, os.SEEK_SET)
    print(file.read(pos))
    file.truncate()
file.close()

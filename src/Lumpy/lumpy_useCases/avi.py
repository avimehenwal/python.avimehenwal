__author__ = 'avimehenwal'

'''
Check if the modules are imported in sys.modules
'swampy': <module 'swampy' from 'C:\\Python34\\lib\\site-packages\\swampy\\__init__.py'>,
'''

import os
import sys
import pprint
sys.path.append('F:\Avi_OpenSource_CoadingPractise\PYTHON\Lumpy\swampy')
# print(sys.path)
# pprint.pprint(sys.modules)

import Lumpy
from build import Build
import subprocess
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

# run the test code
# x = [1, 2, 3]
# y = x
# z = list(x)

# subprocess.Popen("build.py", shell=True)
# a = os.system("build.py")
a = Build()
print(a)
print(type(a))


# draw the current state (relative to the last ref)
lumpy.object_diagram()
lumpy.class_diagram()



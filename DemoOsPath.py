
from os.path import *
from os import *

fileName = "c:\\python310\\python.exe"


if exists(fileName):
    print("파일 있음:{0}".format(getsize(fileName)))
else:
    print("파일 없음")

print(abspath("python.exe"))
print(basename(fileName))

print("우녕이:{0}".format(name))
print("환경이:{0}".format(environ))

import glob
print(glob.glob(r"c:\work\*.py"))

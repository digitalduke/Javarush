import sys
import os

for arg in sys.argv:
    print(arg)

print "PYTHONPATH contains:", sys.path

print "current dir:", os.getcwd()


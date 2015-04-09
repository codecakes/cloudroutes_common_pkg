import os
import sys
import inspect

cur_path = os.path.dirname(os.path.realpath(os.path.abspath(inspect.getfile(inspect.currentframe()))))
if cur_path not in sys.path:
	sys.path.insert(1, cur_path)
	print "common pkg dir name {} added to sys path".format(cur_path)


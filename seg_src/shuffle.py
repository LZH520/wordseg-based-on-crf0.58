#!/usr/bin/env python
#coding: utf-8

import sys
import codecs
import random

reload(sys)
sys.setdefaultencoding("utf-8")


def shuffle(fn):
	"""
	把文件内容打乱，随机化
	"""
	lines = codecs.open(fn, "r", "utf-8").readlines()
	random.shuffle(lines)
	for line in lines:
		print(line.strip())


"""
test module
"""
if __name__=="__main__":
	if len(sys.argv)<2:
		print("Usage:")
		print("\tpython %s  fileName" % sys.argv[0])
	else:
		shuffle(sys.argv[1])

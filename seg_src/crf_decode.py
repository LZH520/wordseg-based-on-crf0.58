#!/usr/bin/env python
#coding: utf-8

import sys
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")

def struct_file(fn):
	"""
	 以空行为分割界线，将文件存到一个数组中，
	 数组元素为数组，例如：
		A
		B

		C
		D
		E
	 则，dat_arr为[ [A, B], [C, D, E] ]
	"""
	dat_arr = []
	dat = []
	with codecs.open(fn, "r", "utf-8") as inf:
		while True:
			line = inf.readline()
			if not line:
				break
			line = line.strip()
			if line == "":
				if len(dat)>0:
					dat_arr.append(dat)
					dat = []
			else:
				dat.append(line)
	return dat_arr

def crf_decode(fn):
	"""
	将CRF标注结果转换成语义标注结果，如：
		我	S
		儿	B
		子	E
		长	B
		大	M
		后	E
		想	S
		当	S
		警	B
		察	E
	转换成:
		我 儿子 长大后 想 当 警察
	"""
	dat_arr = struct_file(fn)
	for i,dat in enumerate(dat_arr):
		sen = ''
		for line in dat:
			word_flag = line.split()
			word = word_flag[0]
			flag = word_flag[-1]
			if flag == 'S':
				sen += word+' '
			elif flag == 'B':
				sen += word
			elif flag == 'M':
				sen += word
			else:
				sen += word +' '
		print(sen.strip())

"""
test module
"""
if __name__=="__main__":
	if len(sys.argv)<2:
		print("Usage:")
		print("\tpython %s  fileName" % sys.argv[1])
	else:
		crf_decode(sys.argv[1])
		

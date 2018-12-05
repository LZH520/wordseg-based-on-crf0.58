#!/usr/bin/env python
#coding: utf-8

import sys
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")

def crf_encode(fn):
	"""
	将已分词的文件转成crf格式的文件，例如:
		明天 早上 去 天津之眼 
			||
		明  B
		天	E
		早  B
		上  E
		去  S
		天  B
		津	M
		之  M
		眼  E
		
	"""
	with codecs.open(fn, "r", "utf-8") as inf:
		while True:
			line = inf.readline()
			flag = ''	  #代表前一个非空字符的state(BMES)
			if not line:
				break
			line = line.strip()
			if len(line) == 0:
				continue
			#判断第一个字符的位置
			if len(line) == 1:
				flag = 'S'
				print("%s	%s" % (line[0], flag))
				print('')
			else:
				if line[1] == ' ' or line[1]=='\t':
					flag = 'S'
					print("%s	%s" % (line[0], flag))
				else:
					flag = 'B'
					print("%s	%s" % (line[0], flag))
				#判断除第一个和倒数第一个字符串的位置
				for i in range(1,len(line)-1):
					c= line[i]
					if c ==' ' or c =='\t':
						continue
					elif  (flag == 'B' or flag == 'M') and (line[i+1] == ' ' or line[i+1] == '\t'):
						flag = 'E'
						print("%s	%s" % (c,flag))
					elif (line[i-1] == ' ' or line[i-1] == '\t') and (line[i+1] == ' ' or line[i+1] == '\t'):
						flag = 'S'
						print("%s	%s" % (c,flag))
					elif (line[i-1] == ' ' or line[i-1] == '\t') and (line[i+1] != ' ' and line[i+1] != '\t'):
						flag = 'B'
						print("%s	%s" % (c,flag))
					else:
						flag = 'M'
						print("%s	%s" % (c, flag))
						
				#判断最后一个字符的位置
				if flag=='M' or flag == 'B':
					flag = 'E'
					print("%s	%s" % (line[-1], flag))
					print('')
				else:
					flag = 'S'
					print("%s	%s" % (line[-1], flag))
					print('')

"""
test module
"""
if __name__=="__main__":
	if len(sys.argv)<2:
		print("Usage:")
		print("\tpython %s fileName" % sys.argv[0])
	else:
		crf_encode(sys.argv[1])


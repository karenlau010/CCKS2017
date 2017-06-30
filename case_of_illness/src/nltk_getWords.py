# coding:utf-8

import nltk
import fio

datadir = "../data2/training dataset v4"
area = ["病史特点", "出院情况", "一般项目", "诊疗经过"]

def getWord(filename):
	lines = fio.ReadFileUTF8(filename)
	
	for line in lines:
		print line.encode('utf-8')
		words = nltk.sent_tokenize(line.encode('utf-8'))
		for word in words:
			wordss = word.word_tokenize(word)
			for wordddd in wordss:
				print worddd


if __name__ == '__main__':
	x = 0
	i = 1
	filename = datadir + '/' + area[x] + '/' + area[x] + '-'+ str(i) +'.txtoriginal.txt'
	getWord(filename)
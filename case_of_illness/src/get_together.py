# coding: utf-8
import fio
import codecs
import sys
import os
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

datadir = "../data/trainingset 1-100/result/病史特点try2"
types = ["body", "check", "disease", "signs", "treatment"]

class result_unit:
    def __init__(self, iname, ileft, iright, itype):
        self.name = iname
        self.left = ileft
        self.right = iright
        self.itype = itype

    def __repr__(self):
        return repr((self.name, self.left, self.right, self.itype))

def trans_type(itype):
    itype = itype.encode('utf-8')
    if itype == "SIGNS":
        return "症状和体征"
    if itype == "CHECK":
        return "检查和检验"
    if itype == "DISEASE":
        return "疾病和诊断"
    if itype == "TREATMENT":
        return "治疗"
    if itype == "BODY":
        return "身体部位"

def get_together(num, itype, total):
    filename = datadir + '/result_' + itype + '-' + str(i) + '.txt'
    #total = []
    lines = fio.ReadFileUTF8(filename)
    for j in range(len(lines)):
        if len(lines[j]) == 0:
            continue
        words = lines[j].split()
        if words[1].startswith('B'):
            cur_type = trans_type(words[1][2:])
            cur_name = ""
            cur_name += words[0]
            cur_left = j
            cur_right = j
            words = lines[j+1].split()
            while words[1].startswith('I'):
                j += 1
                cur_right += 1
                cur_name += words[0]
                words = lines[j+1].split()
            total.append([cur_left, cur_right, cur_name, cur_type])
    return total

if __name__ == '__main__':
    for i in range(91,92):
        total
        for itype in types:
            total = get_together(i, itype)
            # total.sort(key=lambda x:x[2])

            a = np.array(total)
            for (q,w,e,r) in a:
            	print q
            idex=np.lexsort([a[:,1],a[:,0]])
            a_sort=a[idex,:]

            #print sorted(total, key=lambda result_unit: result_unit[1])
            # for cur_result in total:
            #     print cur_result.name, cur_result.left, cur_result.right, cur_result.itype 
            total.sort()
            for name, left, right, itype in a_sort:
                print name, left, right, itype
            # filename = datadir + '/result' + '-' + str(i) + '.txt'
            # fio.AddResult(total, filename)


            
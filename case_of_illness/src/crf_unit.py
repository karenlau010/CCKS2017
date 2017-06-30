# coding:utf-8

import fio
import codecs
import sys
import os
import jieba.posseg as pseg

datadir = "../data2/training dataset v4"
area = ["病史特点", "出院情况", "一般项目", "诊疗经过"]

class CRF_unit:
    def __init__(self):
        self.features = []

    def test_into_aline(self, filename):
        self.features = []
        sentences = fio.ReadFileUTF8(filename);
        for sentence in sentences:
            for token in sentence:
                self.features.append(token)

    def get_posTag(self, sentence):
        words = pseg.cut(sentence)
        return words

    def get_token(self, filename):
        self.features = []
        sentences = fio.ReadFileUTF8(filename);
        for sentence in sentences:
            words = self.get_posTag(sentence)
            for w in words:
                for token in w.word:
                    feature = [token, w.flag, "N"]
                    self.features.append(feature)
                
    def read_type(self, itype):
        itype = itype.encode('utf-8')
        if itype == "症状和体征":
            return "SIGNS"
        if itype == "检查和检验":
            return "CHECK"
        if itype == "疾病和诊断":
            return "DISEASE"
        if itype == "治疗":
            return "TREATMENT"
        if itype == "身体部位":
            return "BODY"


    def get_type(self, filename):
        sentences = fio.ReadFileUTF8(filename);
        for sentence in sentences:
            words = sentence.split()
            print words[-3] + words[-2]
            x = int(words[-3])
            y = int(words[-2])

            #if words[3].encode('utf-8') == "身体部位":
            itype = self.read_type(words[-1])
            self.features[x][2] = "B-" + itype
            for j in range(x+1,y+1):
                self.features[j][2] = "I-" + itype



if __name__ == '__main__':
    extractor = CRF_unit()
    x = 0;
    """
    for i in range(1,241):
        filename = datadir + '/' + area[x] + '/' + area[x] + '-'+ str(i) +'.txtoriginal.txt'
        extractor.get_token(filename)

        filename = datadir + '/' + area[x] + '/' + area[x] + '-'+ str(i) +'.txt'
        extractor.get_type(filename)

        filename = datadir + '/result/' + area[x] + "/" + '1-240_train.txt'
        fio.AddTrain(extractor.features, filename)
    """
    
    for i in range(241, 301):
        filename = datadir + '/' + area[x] + '/' + area[x] + '-'+ str(i) +'.txtoriginal.txt'
        extractor.test_into_aline(filename);

        filename = datadir + '/result/' + area[x] + '.testt-' + str(i) + '.txt'
        fio.AddTest(extractor.features, filename)
    




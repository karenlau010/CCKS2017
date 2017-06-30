#!/bin/bash

for i in {241,300}
do
	crf_test -m ../data2/training dataset v4/result/病史特点/model_1_240 ../data2/training dataset v4/病史特点-i.txt > ../data2/training dataset v4/result/病史特点/result_i.txt
done
#!/bin/bash

for i in {241..300}
do
	crf_test -m model_1_240 病史特点.testt-$i.txt > 病史特点.result-$i.txt
done
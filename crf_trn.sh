#!/bin/bash

CURDIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)

if [ $# -lt 2 ]; then
	echo "Usage:"
	echo "    $0  train_file  model_file"
	exit
fi

if [ ! -f $1 ]; then
	echo "File $1 does not exist!"
	exit
fi

mkdir -p $CURDIR/dat
mkdir -p $CURDIR/res

train_file=$1
model_file=$2

# 先将标注文本打乱
echo "Shuffling label file ..."
python $CURDIR/seg_src/shuffle.py $train_file > $CURDIR/dat/train.shuffle

# 先将输入文件转成crf格式的文件
echo "Converting label file to CRF format ..."
python $CURDIR/seg_src/crf_encode.py $CURDIR/dat/train.shuffle > $CURDIR/dat/crf.trn

# 直接训练
echo "Training ..."
$CURDIR/crf++0.58/crf_learn $CURDIR/seg_src/template.txt $CURDIR/dat/crf.trn $model_file

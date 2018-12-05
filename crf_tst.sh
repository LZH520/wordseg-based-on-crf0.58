#!/bin/bash

CURDIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)

if [ $# -lt 3 ]; then
	echo "Usage:"
	echo "    $0  test_file  model_file  output"
	exit
fi

if [ ! -f $1 ]; then
	echo "file $1 does not exist!"
	exit
fi

test_file=$1
model_file=$2
output=$3

if [ ! -f $2 ]; then
	echo "model not found, did you forget to train a model before testing?"
	exit
fi

python $CURDIR/seg_src/crf_encode.py $1 > $CURDIR/dat/crf.tst

$CURDIR/crf++0.58/crf_test -m $model_file $CURDIR/dat/crf.tst > $CURDIR/res/crf.res.raw

python $CURDIR/seg_src/crf_decode.py $CURDIR/res/crf.res.raw > $output

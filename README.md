# wordseg-based-on-crf++0.58
使用crf++-0.58 实现的分词，并对分词结果进行的评估
要求训练数据和测试数据都是utf-8格式，训练数据是已经分好词的文本文件（分词的分隔符是空格或'\t'）
测试数据是为分词的文本
dat 文件夹中存放了训练数据和测试数据，以及训练和测试中产生的一些中间文件
其中：crf.trn是训练时，crf++0.58训练模型时输入的格式：如：BMES分别代表开始、中间、结束、和单字，每句话以空行分开
     1 妈  B
     2 妈  E
     3 不  S
     4 进  S
     5 被  B
     6 窝  E
     7 你  S
     8 想  S
     9 干  B
    10 什  M
    11 么  E
    12 
    13 什  B
    14 么  E
    15 样  S
    16 能  S
    17 快  B
    18 点  E
    19 升  B
    20 级  E
crf.tst是测试时，crf++0.58测试时输入的格式：如：
     1 扬  B
     2 帆  M
     3 远  M
     4 东  M
     5 做  M
     6 与  M
     7 中  M
     8 国  M
     9 合  M
    10 作  M
    11 的  M
    12 先  M
    13 行  E
    14 
    15 希  B
    16 腊  M
    17 的  M
    18 经  M
    19 济  M
    20 结  M
    21 构  M
    22 较  M
    23 特  M
    24 殊  M
    25 。  E
 ./res/crf.res.raw 是测试时，crf++0.58测试时输出的格式，最后一列是最终的结果，前两列的是输入：如：   
     1 扬  B   B
     2 帆  M   E
     3 远  M   B
     4 东  M   E
     5 做  M   S
     6 与  M   S
     7 中  M   B
     8 国  M   E
     9 合  M   B
    10 作  M   E
    11 的  M   S
    12 先  M   B
    13 行  E   E
    14 
    15 希  B   B
    16 腊  M   E
    17 的  M   S
    18 经  M   B
    19 济  M   M
    20 结  M   E
    21 构  M   B
    22 较  M   E
    23 特  M   B
    24 殊  M   E
    25 。  E   S
因此，需要自己编写代码将文本编译成crf需要的输入格式，以及将crf的输出结果转化成你所需的文本格式
使用步骤：
训练模型：
crf_trn.sh  train_file  model_file
测试模型：
crf_tst.sh  test_file  model_file  output
最后，seg_src文件夹中有评估分词结果的工具：seg_eval.py
使用方法：
python seg_eval.py  ref_file  ans_file  eval_file
计算结果中有准确率，召回率，F1和错误率，输出结果格式如：eval.res



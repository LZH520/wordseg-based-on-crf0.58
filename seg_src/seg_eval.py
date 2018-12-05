# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:30:20 2018

@author: zihua.li
"""

"""
以下面的分词结果为例：
“计算机 总是 有问题”——黄金标准
“计算机 总 是 有问题”——待评测的结果
 
给分出来的每个词都做位置的标记（位置从1开始）：
[[1,2,3],[4,5],[6,7,8]] ——黄金标准
[[1,2,3],[4],[5],[6,7,8]] ——待评测的结果
"""
import codecs
import sys
import re

def get_position_index(sen):
    #sen_nospace = sen.replace(' ','')
    sen_nospace = re.sub(r' ','',sen)
    word_idx =[]
    sen_idx = []
    i = 0
    while (i < len(sen)):
        if sen[i] != ' ':
            index = sen_nospace.index(sen[i])
            word_idx.append(index+1)
            i +=1
            if i == len(sen)-1:
                sen_idx.append(tuple(word_idx))  
        else:
            i +=1
            sen_idx.append(tuple(word_idx))
            word_idx = []
    return sen_idx

def cal_prf(ref_inf,ans_inf,analys_outf):
    ref_f = codecs.open(ref_inf, "r", "utf-8")
    ans_f = codecs.open(ans_inf, "r", "utf-8")
    analys_f = codecs.open(analys_outf,'w','utf-8')
    """
    N ：黄金标准分割的总单词数; n:每句黄金标准分隔的单词数
    E ：分词器错误标注的总单词数; e:每句分词器错误标注的单词数
    C ：分词器正确标注的总单词数; c:每句分词器正确标注的单词数
    """
    N=0;E=0;C=0
    num = 0
    while True:
        ref_line = ref_f.readline().strip()
        ans_line = ans_f.readline().strip()
        #print(ref_line)
        n=0;e=0;c=0
    		# 若两个文件的行数不一致，则退出
        if not ref_line:
            if not ans_line:
                break
            else:
                print("sentence number not equal!")
                exit()
        else:
            if not ans_line:
                print("sentence number not equal!")
                exit()
        num += 1
        #ref_nospace = ref_line.replace(' ','')
        #ans_nospace = ans_line.repalce(' ','')
        ref_nospace = re.sub(r' ','',ref_line)
        ans_nospace = re.sub(r' ','',ans_line)

    		# 若句子不相同，则退出
        if ref_nospace != ans_nospace:
            print("The %dth line of two files are different!" % num)
            exit()
        analys_f.write('sentence: '+ ref_nospace + '\n')
        analys_f.write('ref: '+ ref_line + '\n')
        analys_f.write('ans: '+ ans_line+ '\n')
        
        #对每句计算n,e,c
        ref_post = get_position_index(ref_line)
        ans_post = get_position_index(ans_line)
        n = len(ref_post)
        c = len(set(ref_post).intersection(set(ans_post)))
        e =  len(set(ref_post).difference(set(ans_post)))
        analys_f.write('[word_num : %d] [err_num: %d] [correct_num: %d]'%(n,e,c)+'\n')
        N += n
        C += c
        E += e
    #统计结束，计算准确率、召回率、F1
    if C == 0 and E == 0:
        precision = "Nan"
    else:
        precision = C*1.0/(C+E)
    if N == 0:
        recall = "Nan"
        error_rate = "Nan"
    else:
        recall = C*1.0/N
        error_rate = E*1.0/N
    if recall == 0 and precision == 0:
        f1 = "Nan"
    else:
        rp = recall*precision
        f1 = 2.0*rp/(precision + recall)
        analys_f.write('*'*30+' RESULT '+'*'*30+'\n')
        analys_f.write('[word_num_total : %d] [err_num_total: %d] [correct_num_total: %d]'%(N,E,C)+'\n')
        analys_f.write("evaluate result: Precision:%.4f  Recall:%.4f  F1:%.4f   ErrorRate:%.4f " % (precision,recall,f1,error_rate))
    ref_f.close()
    ans_f.close()
    analys_f.close()
    
        
if __name__ == '__main__':
    if len(sys.argv)<4:
        print("Usage:")
        print("\tpython %s  ref_file  ans_file  eval_file")
    else:
        cal_prf(sys.argv[1], sys.argv[2], sys.argv[3])

    
    

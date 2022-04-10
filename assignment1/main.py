import numpy as np
import pandas as pd
from itertools import combinations
from sklearn.svm import l1_min_c

df = []
# with open(r'C:\Users\gc949\Desktop\Assignment1\browsing.txt') as d:
with open(r'browsing.txt') as d:
    for line in d.readlines():
        data = line.split('\n\t')
        for string in data:
            tmp_str = string.strip('\n').split(' ')
        if tmp_str:
            df.append(tmp_str[:-1])

print(df[0][1])

def dictionary(dataset):
    f = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in f:
                f.append([item])
    f.sort()

    return list(map(dictionary,f))

def fliter(ds,dk):
    N = float(len(ds))
    support_data = {}
    Set = {}
    for i in ds:
        for j in dk:
            if j.issubset(i): #判断j是否是i的子集
                if j not in Set:
                    Set[j] = 1
                else:
                    Set[j] += 1 #记录次数
    relist = [] #满足条件的数据
    for k in Set:
        support = Set[k]
        if support >= 100:
            relist.insert(0,k)
        support_data[k] = support
    return relist, support_data


#测试L1 输出结果647
test_data = list(map(set,df))
test0 = dictionary(df)
test = fliter(test_data,test0)

Set = {}
for i in test_data:
    for j in test0:
        if j.issubset(i): #判断j是否是i的子集
            if j not in Set:
                Set[j] = 1
            else:
                Set[j] += 1 #记录次数，没有就是1，如果集合里有就是+1
relist = [] #满足条件的数据
for k in Set:
        support = Set[k]
        if support >= 100:
            relist.insert(0,k)
print(len(relist))
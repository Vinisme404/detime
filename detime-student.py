# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:21:17 2021

@author: lilin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:01:37 2021

@author: lilin
"""
import random
import time

#字符串长度
length = 8000000 #值太小会出现计时偏差错误


def different_time_compare(val1, val2):
    t1 = time.time()
    if len(val1) != len(val2):
        return False
    for i in range(len(val2)):
        if val1[i] != val2[i]:
            t2 = time.time()
            runTime = t2 - t1
            return  False,runTime
        time.sleep(0.1)
    t2 = time.time()
    runTime = t2 - t1
    return True,runTime



def constant_time_compare(val1, val2):
    t1 = time.time()
    if len(val1) != len(val2):
        return False
    result = 0
    for x, y in zip(val1, val2):#补充：
        result |= ord(x) ^ ord(y)
    t2 = time.time()
    runTime = t2 - t1
    return result == 0,runTime

    
#生成字符串  
seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
str1 = []
for i in range(length):
  str1.append(random.choice(seed))
Stringright = ''.join(str1)


str2 = []
for i in range(length):
  str2.append(random.choice(seed))
Stringguess = ''.join(str2)


result = different_time_compare("abcdef", "abcdee")
print(result)
result = different_time_compare("abcdef", "abcdef")
print(result)
result = constant_time_compare("abcdef", "abcdee")
print(result)
result = constant_time_compare("abcdef", "abcdef")
print(result)



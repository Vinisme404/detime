# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:48:11 2021

@author: lilin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:02:02 2021

@author: lilin
"""

#import login
import time
import sys
 
length = 4
times = 100
password = "asss"

# 模拟登陆等字符串验证过程 
def login(input):
    for i in range(0,len(input)):
        if password[i] != input[i]:
            return False
        # 模拟延时
        time.sleep(0.00001)
    return True


# 获取密码验证耗费时间
def getRunTime(input):
    t1 = time.time()
    # 多次验证，累计时间
    for i in range(int(times)):
        login(input)
    t2 = time.time()
    runTime = t2 - t1
    return runTime
 
 
if __name__ == "__main__":
 
    result = ""
    for index in range(length):
        # 验证次数随已猜测字符串长度增加而减少
        times/=(index+1)
        #补充
        maxTime = 0
        bestLetter = ''
        for i in range(26):
            letter = chr(ord('a')+i)
            runTime = getRunTime(result+letter)
            if runTime > maxTime:
                maxTime = runTime
                bestLetter = letter
        result += bestLetter
        #补充

        print(str(index/length*100)+"%")
    print("100.0%")
    print(runTime)
    print(times)
    print(result)
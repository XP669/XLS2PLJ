import time
import sys
import re
import os
import random
import SFExampleTable2

"""
dict = {};
#先构造一个100000元素的大字典
i = 0
while (i<100000):
    key0 = '%05d' % i
    dict[key0] = i * i + 3 * i + 5
    i = i+1
#测试has_key指令查找key值100000次
i = 0
count = 0
t0 = time.time()
while(i < 100000):
    count += dict['99999']
    i+=1
t1 = time.time() - t0
print("spent %f seconds, found %d key" % (t1, count))


dict2 = {};
#先构造一个100000元素的大字典
i = 0
while (i<100000):
    dict2[i] = i * i + 3 * i + 5
    i = i+1
#测试has_key指令查找key值100000次
i = 0
count = 0
t0 = time.time()
while(i < 100000):
    count += dict2[i]
    i+=1
t1 = time.time() - t0
print("spent %f seconds, found %d key" % (t1, count))

"""

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__

print (SFExampleTable2.groupData2[1]['vector2ds'])





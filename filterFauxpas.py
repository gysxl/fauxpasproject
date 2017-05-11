#!/usr/bin/python
import os
import re
from itertools import islice

lines = open('result2.txt').readlines()
if os.path.exists('result2_replace.txt'):
    os.remove('result2_replace.txt')
if os.path.exists('result.txt'):
    os.remove('result.txt')
fp = open('result2_replace.txt','wb')
fp_result = open('result.txt','wb')
for s in lines:
    fp.write(s.replace('CONCERN:','CONCERN:CONCERN1:').replace('WARNING:','WARNING:WARNING2:').replace('ERROR:','ERROR:ERROR3:'))
fp.close()

fp = open('result2_replace.txt').read()
fp_list = re.split('CONCERN:|WARNING:|ERROR:',fp)

leng = len(fp_list)

for li in fp_list:
    m = re.search('Sofa',li)
    if m is not None:
        fp_result.write(li.split('\n')[0])
        fp_result.write('\n')
        # print li.split('\n')[0]
        list2 = re.split('~+',li[len(li.split('\n')[0]):])
        for li2 in list2:
            n = re.search('Sofa',li2)
            if n is not None:
                print li2
                fp_result.write(li2)
                fp_result.write('\n')
                fp_result.write('                 ~~~~~~~~~~~~')
                fp_result.write('\n')
            else:
                print 'not match sofa'
        # fp_result.write(li.)
        print "matched!"
    else:
        print "not match!"

fp_result.close()

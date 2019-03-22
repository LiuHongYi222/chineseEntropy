# _*_ coding:utf-8 _*_
import os

def precessSpe(input):

    output = input.replace(' ','').replace('\n','，').replace('  ','') \
                .replace('\r\n', ',')
    return  (output)


def loadData(filePath):

    f = open(filePath,'rb')
    output =''
    for line in f.readlines():
        senten = (line.decode('gbk','ignore'))
        output +=(precessSpe(senten))

    f.close()
    return output

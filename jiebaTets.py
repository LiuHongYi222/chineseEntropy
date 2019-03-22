# encoding=utf-8
import os
import loadData
from math import log
import jieba.posseg as pseg


count =0
shannonEnt = float(0.0)
numEntries = 0
# save whole words and counts from corpus
labelCounts = {}
#save entropy for every word
dict1 ={}

logFile = open('log.txt','w')
rootDir = r'C:\Users\GENIUS\Desktop\搜狗分类新闻.20061127\SogouC.reduced\Reduced'


for dirpath  in os.listdir(rootDir):


    logFile.write(rootDir +'\\'+dirpath +'\n')

    for filename in os.listdir(rootDir + '\\' + dirpath):

        count += 1
        if (count % 100 == 0):
            logFile.write(' 100  files  searched \n')

        print('File: ',os.path.join(dirpath, filename),'is counting entropy... ')

        words = loadData.loadData(
            os.path.join(rootDir + '\\' +dirpath+ '\\' +filename))

        words = pseg.cut(words)

        wordList =[]
        #each word in a file(namely a journalism)
        for word,flag in words:

            #only concern  the word that contains chinese
            for chars in word:
                if ('\u4e00' <= chars <= '\u9fa5'):
                    # wordList.append([word,flag])
                    wordList.append(word)
                    break

        numEntries += len(wordList)


        for featVec in wordList:
            currentLabel = featVec
            if currentLabel not in labelCounts.keys():
                labelCounts[currentLabel]=0
            labelCounts[currentLabel]+=1
    # break

logFile.close()

print(len(labelCounts))
print(numEntries)

for key in labelCounts:
    prob = float(labelCounts[key])/numEntries
    shannonEnt += -prob * log(prob,2)
    dict1[key] = -prob * log(prob,2)


validShannonEnt =0
entFile = open('wordEntro.txt','w')
for key,value in dict1.items():
    entFile.write('{key}:{value}\n'.format(key = key, value = value))
    validShannonEnt += value
entFile.close()

print(validShannonEnt)
print(shannonEnt)


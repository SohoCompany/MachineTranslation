import numpy as np
import math

oneGramDict = {}
oneGramConditionDict = {}

biGramDict = {}
biGramConditionDict = {}

triGramDict = {}
triGramConditionDict = {}

DictSequence = [oneGramDict, biGramDict, triGramDict]
ConditionDictSequence = [oneGramConditionDict, biGramConditionDict, triGramConditionDict]

oneGramWordCount = 0
biGramWordCount = 0
triGramWordCount = 0

#TODO
oneGramModelFileName = "sourceCorpusOneGramModel.txt"
biGramModelFileName = "sourceCorpusBiGramModel.txt"
triGramModelFileName = "sourceCorpusTriGramModel.txt"
sourceFileName = ""
targetFileName = ""
firstFlag = '@' 
secondFlag = '#'

def loadModel(modelFileName, wordCountDict, conditionWordCountDict, wordCount):
	modelFile = open(modelFileName)
	lineList = modelFile.readlines()
	for line in lineList:
		if line[0] == firstFlag:
			currentPair = line.split(firstFlag)
			#print(currentPair[1], int(currentPair[2]))
			wordCount += int(currentPair[2])
			wordCountDict[currentPair[1]] = int(currentPair[2])
		if line[0] == secondFlag:
			currentPair = line.split(secondFlag)
			#print(currentPair[1], currentPair[2], int(currentPair[3]))
			if conditionWordCountDict.has_key(currentPair[1]):
				currentDict = conditionWordCountDict[currentPair[1]]
				currentDict[currentPair[2]] = int(currentPair[3])
			else :
				currentDict = {currentPair[2]: int(currentPair[3])}
				conditionWordCountDict[currentPair[1]] = currentDict


#1 Laplace平滑 2 对于没有出现过的串和单个字符要怎么处理
#忽略在字符表中没有出现过的字符，然为是字符表中的某个字符
#如果一个串在语料中没有出现过，则可以认为是不可能事件，不可能事件的熵为0,不可能事件的条件熵为0
def caculateConditionEntropy(sentence):
	length = len(sentence)
	currentDict = DictSquence[length - 1]
	currentConditionDict = ConditionDictSequence[length - 1]
	characterDict = DictSequence[0]
	if currentDict.has_key(sentence):#如果一个串，从来都是出现在一句话的最后，那么这句话会出现在Dict里，但是不会出现在Condition Dict里

		differentCharacterCount = len(characterDict)#一元模型的长度，等于一共有多少个不同的字符
		existCharacterCount = 0
		if currentConditionDict.has_key(sentence):
			existCcharacterCount = len(currentConditionDict[sentence])
		else:
		smoothParameter = currentDict[sentence] + differentCharacterCount - existCharacterCount

		conditionEntropy = 0
		for key in characterDict.keys():
			if currentConditionDict[sentence].has_key(key):
				currentProbability = currentConditionDict[sentence][key]/smoothParameter
				currentEntropy = -1*currentProbability*math.log(currentProbability)
				conditionEntropy = conditionEntropy + currentEntropy
			else:
				currentProbability = 1/smoothParameter
				currentEntropy = -1*currentProbability*math.log(currentProbability)
				conditionEntropy = conditionEntropy + currentEntropy

	else:
		return 0.0

#最长长度取3的话，只需要从前向后一直到lenght-3
def processSentence(sentence):
	posSet = set()
	length = len(sentence)
	for i in range(length - 2):
		tempEntropy1 = caculateConditionEntropy(sentence[i])
		tempEntropy2 = caculateConditionEntropy(sentence[i] + sentence[i+1])
		tempEntropy3 = caculateConditionEntropy(sentence[i] + sentence[i+1] + sentence[i+2])
		if tempEntropy2 > tempEntropy1
			posSet.add(i+1)
		if tempEntropy3 > tempEntropy2
			posSet.add(i+2)
	if (length - 1) in posSet:#最后一个位置不用加入空格
		posSet.remove(length - 1)
	result = ""
	for i in range(length):
		result = result + sentence[i]
		if i in posSet:
			result = result + ' '
	return result
	

def doSegmention(sourceFileName, targetFileName) :
	loadModel(oneGramModelFileName, oneGramDict, oneGramConditionDict, oneGramWordCount)
	loadModel(biGramModelFileName, biGramDict, biGramConditionDict, biGramWordCount)
	loadModel(triGramModelFileName, triGramDict, triGramConditionDict, triGramWordCount)
	sourceFile = open(sourceFileName)
	targetFile = open(targetFileName, 'w+')
	lineList = sourceFile.readlines()
	for line in lineList:
		sentence = line.split()
		characters = sentence[0]
		result = processSentence(characters)
		targetFile.write(result)
	sourceFile.close()
	targetFile.close()

doSegmention(sourceFileName, targetFileName)


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

'''
oneGramWordCount = 0
biGramWordCount = 0
triGramWordCount = 0
'''

#TODO
oneGramModelFileName = "../Model/sourceCorpus1Gram.txt"
biGramModelFileName = "../Model/sourceCorpus2Gram.txt"
triGramModelFileName = "../Model/sourceCorpus3Gram.txt"
sourceFileName = "../sourceCorpus.txt"
targetFileName = "../sourceCorpusSegmented.txt"
firstFlag = '@' 
secondFlag = '#'

def loadModel(modelFileName, wordCountDict, conditionWordCountDict):
	modelFile = open(modelFileName)
	lineList = modelFile.readlines()
	for line in lineList:
		if line[0] == firstFlag:
			currentPair = line.split(firstFlag)
			#print(currentPair[1], int(currentPair[2]))
			#wordCount = wordCount + int(currentPair[2])
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


def caculateConditionEntropy(sentence):
	length = len(sentence)
	global DictSequence
	global ConditionDictSequence
	currentDict = DictSequence[length - 1]
	currentConditionDict = ConditionDictSequence[length - 1]
	characterDict = DictSequence[0]
	if currentDict.has_key(sentence):
		#print("has_key:" + sentence)
		differentCharacterCount = len(characterDict)
		existCharacterCount = 0
		smoothParameter = currentDict[sentence]

		if currentConditionDict.has_key(sentence):
			existCharacterCount = len(currentConditionDict[sentence])

		smoothParameter = currentDict[sentence] + differentCharacterCount - existCharacterCount
		#print(differentCharacterCount, existCharacterCount, smoothParameter, currentDict[sentence])	

		conditionEntropy = 0.0
		for key in characterDict.keys():
			if currentConditionDict[sentence].has_key(key):
				#print("has_key has_key:" + key)
				#currentProbability = currentConditionDict[sentence][key]/smoothParameter
				currentEntropy = currentConditionDict[sentence][key]*math.log(smoothParameter/currentConditionDict[sentence][key])/smoothParameter
				#print(currentConditionDict[sentence][key], smoothParameter)
				conditionEntropy = conditionEntropy + currentEntropy
			else:
				#print("has_key do not has_key:" + key)
				#currentProbability = 1/smoothParameter
				currentEntropy = math.log(smoothParameter)/smoothParameter
				#print(1, smoothParameter)
				conditionEntropy = conditionEntropy + currentEntropy
		return conditionEntropy

	else:
		#print("do not has key:" + sentence)
		return 0.0

def processSentence(sentence):
	posSet = set()
	length = len(sentence)
	for i in range(length - 2):
		word1 = ""
		word2 = ""
		word3 = ""
		word1 = word1 + sentence[i]
		word2 = word2 + sentence[i] + sentence[i+1]
		word3 = word3 + sentence[i] + sentence[i+1] + sentence[i+2]
		tempEntropy1 = caculateConditionEntropy(word1)
		tempEntropy2 = caculateConditionEntropy(word2)
		tempEntropy3 = caculateConditionEntropy(word3)
		'''
		print(word1, tempEntropy1)
		print(word2, tempEntropy2)
		print(word3, tempEntropy3)
		'''
		if tempEntropy2 > tempEntropy1:
			posSet.add(i+1)
		if tempEntropy3 > tempEntropy2:
			posSet.add(i+2)
	if (length - 1) in posSet:
		posSet.remove(length - 1)
	result = ""
	for i in range(length):
		result = result + sentence[i]
		if i in posSet:
			result = result + ' '
	return result
	

def doSegmention(sourceFileName, targetFileName) :
	loadModel(oneGramModelFileName, oneGramDict, oneGramConditionDict)
	loadModel(biGramModelFileName, biGramDict, biGramConditionDict)
	loadModel(triGramModelFileName, triGramDict, triGramConditionDict)
	sourceFile = open(sourceFileName)
	targetFile = open(targetFileName, 'w+')
	lineList = sourceFile.readlines()
	for line in lineList:
		sentence = line.split()
		characters = sentence[0]
		result = processSentence(characters)
		targetFile.write(result + '\n')
	sourceFile.close()
	targetFile.close()
	'''
	sentence = "COc1cccc(NC(EO)OC(C)(C)C)c1I"
	result = processSentence(sentence)
	print(result)
	'''


doSegmention(sourceFileName, targetFileName)


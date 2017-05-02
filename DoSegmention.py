oneGramDict = {}
oneGramConditionDict = {}

biGramDict = {}
biGramConditionDict = {}

triGramDict = {}
triGramConditionDict = {}

oneGramWordCount = 0
biGramWordCount = 0
triGramWordCount = 0

#TODO
oneGramModelFileName = "sourceCorpusOneGramModel.txt"
biGramModelFileName = "sourceCorpusBiGramModel.txt"
triGramModelFileName = "sourceCorpusTriGramModel.txt"
'''
oneGramModelFileName = "targetCorpusOneGramModel.txt"
biGramModelFileName = "targetCorpusBiGramModel.txt"
triGramModelFileName = "targetCorpusTriGramModel.txt
'''
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

loadModel(oneGramModelFileName, oneGramDict, oneGramConditionDict, oneGramWordCount)
loadModel(biGramModelFileName, biGramDict, biGramConditionDict, biGramWordCount)
loadModel(triGramModelFileName, triGramDict, triGramConditionDict, triGramWordCount)

def processSentence(sentence):


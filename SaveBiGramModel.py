wordCountDict = {}
conditionWordCountDict = {}
wordCount = 0
firstFlag = '@'
secondFlag = '#'
sourceFileName = "test.txt"
targetFileName = "target2.txt"

def processSentence(line):
	sentence = line.split()
	characters = sentence[0]
	length = len(characters)
	global wordCount
	wordCount = (wordCount + length - 1)
	for i in range(length):
		if i < length - 1 :
			currentWord = characters[i] + characters[i+1]
			if wordCountDict.has_key(currentWord) :
				wordCountDict[currentWord] = wordCountDict[currentWord] + 1
			else :
				wordCountDict[currentWord] = 1
		if i < length - 2 :
			currentWord = characters[i] + characters[i+1]
			if conditionWordCountDict.has_key(currentWord):
				currentDict = conditionWordCountDict[currentWord]
				if currentDict.has_key(characters[i+2]):
					currentDict[characters[i+2]] = currentDict[characters[i+2]] + 1
				else:
					currentDict[characters[i+2]] = 1
			else:
				currentDict = {characters[i+2]:1}
				conditionWordCountDict[currentWord] = currentDict


def saveModel(sourceFileName, targetFileName):
	sourceFile = open(sourceFileName)
	lineList = sourceFile.readlines()
	for line in lineList:
		processSentence(line)
	targetFile = open(targetFileName, 'w+')
	wordCountPairs = wordCountDict.items()
	for i in range(len(wordCountPairs)):
		currentPair = wordCountPairs[i]
		targetFile.write(firstFlag+currentPair[0]+firstFlag+str(currentPair[1])+ '\n')

	conditionCountPairs = conditionWordCountDict.items()
	for i in range(len(conditionCountPairs)):
		currentPair = conditionCountPairs[i]
		firstKey = currentPair[0]
		currentDict = currentPair[1]
		tempPairs = currentDict.items()
		for j in range(len(tempPairs)):
			tempPair = tempPairs[j]
			targetFile.write(secondFlag+firstKey+secondFlag+tempPair[0]+secondFlag+str(tempPair[1])+'\n')
'''
print(wordCount)
print(wordCountDict)
print(conditionWordCountDict)
'''
saveModel(sourceFileName, targetFileName)

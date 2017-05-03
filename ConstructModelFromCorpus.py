wordCountDict = {}
conditionWordCountDict = {}
wordCount = 0
firstFlag = '@'
secondFlag = '#'
sourceFileName = "../targetCorpus.txt"
gram = 4
targetFileName = "../Model/targetCorpus" + str(gram) + "Gram.txt"

def processSentence(line):
	sentence = line.split()
	characters = sentence[0]
	length = len(characters)
	global wordCount
	wordCount = (wordCount + length - gram + 1)
	for i in range(length):
		if i < length - gram + 1 :
			currentWord = ""
			for j in range(gram):
				currentWord = currentWord + characters[i+j]

			if wordCountDict.has_key(currentWord) :
				wordCountDict[currentWord] = wordCountDict[currentWord] + 1
			else :
				wordCountDict[currentWord] = 1
		if i < length - gram :
			currentWord = ""
			for j in range(gram):
				currentWord = currentWord + characters[i+j]

			if conditionWordCountDict.has_key(currentWord):
				currentDict = conditionWordCountDict[currentWord]
				if currentDict.has_key(characters[i+gram]):
					currentDict[characters[i+gram]] = currentDict[characters[i+gram]] + 1
				else:
					currentDict[characters[i+gram]] = 1
			else:
				currentDict = {characters[i+gram]:1}
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
	sourceFile.close()
	targetFile.close()
'''
print(wordCount)
print(wordCountDict)
print(conditionWordCountDict)
'''
saveModel(sourceFileName, targetFileName)


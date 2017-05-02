wordCountDict = {}
conditionWordCountDict = {}
wordCount = 0
firstFlag = '@'
secondFlag = '#'
#sourceFileName = "test.txt"
modelFileName = "target.txt"

def loadModel(modelFileName):
	modelFile = open(modelFileName)
	lineList = modelFile.readlines()
	global wordCount
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
	
loadModel(modelFileName)
print(wordCount)
print(wordCountDict)
print(conditionWordCountDict)

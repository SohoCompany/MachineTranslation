import numpy as np

dictFileName = "../Corpus/sourceCorpusSegmentedVec.txt"
wordDict = {}

def loadDict(dictFileName, wordDict): 
	dictFile = open(dictFileName)
	firstLine = dictFile.readline()
	firstSentence = firstLine.split()
	totalLength = firstSentence[0]
	#totalLength = 1
	dimension = firstSentence[1]
	print(totalLength, dimension)
	for i in range(int(totalLength)):
		currentSentence = dictFile.readline()
		wordAndVec = currentSentence.split()
		word = wordAndVec[0]
		currentVec = np.zeros([int(dimension), 1])
		for j in range(int(dimension)):
			currentVec[j] = wordAndVec[j+1]
		wordDict[word] = currentVec
		print(word)
		print(currentVec)
	dictFile.close()
loadDict(dictFileName, wordDict)


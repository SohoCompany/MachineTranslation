def processData(sourceFileName, sourceLanguageFile, targetLanguageFile):
	sourceFile = open(sourceFileName)
	sourceLanFile = open(sourceLanguageFile, 'w+')
	targetLanFile = open(targetLanguageFile, 'w+')
	lineList = sourceFile.readlines()
	for line in lineList:
		sentences = line.split('>>')
		sourceSentence = sentences[1]
		targetSentence = sentences[0]
		sourceLanFile.write(sourceSentence)
		targetLanFile.write(targetSentence + '\n')
	sourceFile.close()
	sourceLanFile.close()
	targetLanFile.close()

sourceFileName = '../train.txt'
sourceLanguageFile = 'sourceCorpus.txt'
targetLanguageFile = 'targetCorpus.txt'
processData(sourceFileName, sourceLanguageFile, targetLanguageFile)

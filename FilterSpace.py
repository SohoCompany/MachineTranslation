sourceFileName="/home/zhenzhuo/WorkSpace/MTTest2*128/Corpus/test.translated.en"
targetFileName="/home/zhenzhuo/WorkSpace/MTTest2*128/Corpus/test.translated.nospace.en"

def processFile(sourceFileName, targetFileName):
	sourceFile = open(sourceFileName)
	targetFile = open(targetFileName, 'w+')
	lineList = sourceFile.readlines()
	for line in lineList:
		sentence = ''.join(line.split())
		targetFile.write(sentence + '\n')
	sourceFile.close()
	targetFile.close()

processFile(sourceFileName, targetFileName)



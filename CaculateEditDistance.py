from Levenshtein import *

sourceFileName = "/home/zhenzhuo/WorkSpace/MTTest2*128/Corpus/test.nospace.en"

targetFileName = "/home/zhenzhuo/WorkSpace/MTTest2*128/Corpus/test.translated.nospace.en"

size = 1000

def caculateEditDistance(sourceFileName, targetFileName, size):
	sourceFile = open(sourceFileName)
	targetFile = open(targetFileName)
	totalDistance = 0.0
	for i in range(size):
		sourceLine = sourceFile.readline()
		targetLine = targetFile.readline()
		print("sourceLine:", sourceLine)
		print("targetLine:", targetLine)
		totalDistance = totalDistance + distance(sourceLine, targetLine)		
	print("Average edit distance:", totalDistance/size)
	sourceFile.close()
	targetFile.close()

caculateEditDistance(sourceFileName, targetFileName, size)

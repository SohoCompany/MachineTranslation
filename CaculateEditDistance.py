from Levenshtein import *

sourceFileName = "test1.txt"
targetFileName = "test2.txt"
size = 4

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

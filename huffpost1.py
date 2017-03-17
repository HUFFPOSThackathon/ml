import csv
import random
import math
def loadcsv(filename):
	lines=csv.reader(open(filename,"rb"))
	dataset=list(lines)
	for i in range(len(dataset)):
			dataset[i]=[x for x in dataset[i]]
	return dataset
def seperateByClass(dataset):
	seperated={}
	for i in range(len(dataset)):
		vector=dataset[i]
		vector[2]=vector[2].lower()
		if vector[2] not in seperated:
			seperated[vector[2]]=0
	for i in range(len(dataset)):
		vector=dataset[i]
		seperated[vector[2]]=seperated[vector[2]]+1
	return seperated

def summarize(state,dataset):
	summaries=''
	for value in dataset:
		summaries=summaries+value+" won "+str(dataset[value])+" seats , "
	summaries=summaries+"in"+state
	return summaries
def summarizeByClass(state,dataset):
	seperated={}
	seperated=seperateByClass(dataset)
	summaries={}
	for classvalue,instances in seperated.iteritems():
		summaries[classvalue]=summarize(state,instances)
	return summaries

def summarizeByClass(dataset):
	seperated={}
	seperated=seperateByClass(dataset)
	summaries=summarize(seperated)
	return summaries


def statesumm(state,filename):
	dataset=loadcsv(filename)
	summ=summarizeByClass(state,dataset)
	print summ
main()

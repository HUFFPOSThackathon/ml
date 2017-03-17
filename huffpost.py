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
	vector=[]
	for i in range(len(dataset)):
		vector=dataset[i]
		vector[1]=vector[1].lower()
		if vector[1] not in seperated:
			seperated[vector[1]]=vector
	return seperated

def summarize(dataset):
	summaries=' '
	summaries=summaries+dataset[3]+" from "+dataset[2]+" won from constituency "+dataset[1]+" by "+dataset[-1]+" percentage of votes "
	return summaries
def summarizeByClass(dataset):
	seperated={}
	seperated=seperateByClass(dataset)
	summaries={}
	for classvalue,instances in seperated.iteritems():
		summaries[classvalue]=summarize(instances)
	return summaries

def summarizeByClass(dataset):
	seperated={}
	seperated=seperateByClass(dataset)
	summaries={}
	for classvalue,instances in seperated.iteritems():
		summaries[classvalue]=summarize(instances)
	return summaries


def constsummary(test,filename):
	dataset=loadcsv(filename)
	summ=summarizeByClass(dataset)
	print summ[test]
main()

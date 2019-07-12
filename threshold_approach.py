import numpy
organ_score=numpy.loadtxt(fname='threshold_approach-organ_score.txt', dtype=int)

organ_score.shape
len(organ_score)

thresholds=[]
num_of_thresholds=range(0,len(organ_score))

from scipy import stats

for i in reversed(num_of_thresholds):
    temp_threshold=stats.norm.ppf((len(num_of_thresholds)-i)/len(num_of_thresholds), loc=100, scale=20)
    thresholds.append(temp_threshold)

thresholds.insert(0,float("-inf"))

print('the trhesholds are:\n', thresholds)

for j in range(0, len(organ_score)):
    upper_limit_index=numpy.searchsorted(thresholds, organ_score[j], side='right')
    print('organ nubmer ', j, ' is in interval [',thresholds[upper_limit_index-1],'-', thresholds[upper_limit_index],')')
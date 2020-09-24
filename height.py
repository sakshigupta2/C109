import pandas as pd 
import statistics
import csv
df = pd.read_csv("data.csv")
heightlist = df["Height(Inches)"].to_list()
weightlist = df["Weight(Pounds)"].to_list()
heightmean = statistics.mean(heightlist)
weightmean = statistics.mean(weightlist)
heightmedian = statistics.median(heightlist)
weightmedian = statistics.median(weightlist)
heightmode = statistics.mode(heightlist)
weightmode = statistics.mode(weightlist)
print("Mean, Median, Mode of Height Is:- {}, {}, {} respectively".format(heightmean, heightmedian, heightmode))
print("Mean, Median, Mode of Weight Is:- {}, {}, {} respectively".format(weightmean, weightmedian, weightmode))
heightstdDev = statistics.stdev(heightlist)
weightstdDev = statistics.stdev(weightlist)
height1stdDevStart, height1stdDevEnd = heightmean - heightstdDev, heightmean + heightstdDev
height2stdDevStart, height2stdDevEnd = heightmean - (2*heightstdDev), heightmean + (2*heightstdDev)
height3stdDevStart, height3stdDevEnd = heightmean - (3*heightstdDev), heightmean + (3*heightstdDev)
weight1stdDevStart, weight1stdDevEnd = weightmean - weightstdDev, weightmean + weightstdDev
weight2stdDevStart, weight2stdDevEnd = weightmean - (2*weightstdDev), weightmean + (2*weightstdDev)
weight3stdDevStart, weight3stdDevEnd = weightmean - (3*weightstdDev), weightmean + (3*weightstdDev)
heightDataWithin1std = [result for result in heightlist if result > height1stdDevStart and result < height1stdDevEnd]
heightDataWithin2std = [result for result in heightlist if result > height2stdDevStart and result < height2stdDevEnd]
heightDataWithin3std = [result for result in heightlist if result > height3stdDevStart and result < height3stdDevEnd]
weightDataWithin1std = [result for result in weightlist if result > weight1stdDevStart and result < weight1stdDevEnd]
weightDataWithin2std = [result for result in weightlist if result > weight2stdDevStart and result < weight2stdDevEnd]
weightDataWithin3std = [result for result in weightlist if result > weight3stdDevStart and result < weight3stdDevEnd]
print("{} % Of Height Data lies within 1st Standard Deviation".format(len(heightDataWithin1std)*100/len(heightlist)))
print("{} % Of Height Data lies within 2nd Standard Deviation".format(len(heightDataWithin2std)*100/len(heightlist)))
print("{} % Of Height Data lies within 3rd Standard Deviation".format(len(heightDataWithin3std)*100/len(heightlist)))
print("{} % Of Weight Data lies within 1st Standard Deviation".format(len(weightDataWithin1std)*100/len(weightlist)))
print("{} % Of Weight Data lies within 2nd Standard Deviation".format(len(weightDataWithin2std)*100/len(weightlist)))
print("{} % Of Weight Data lies within 3rd Standard Deviation".format(len(weightDataWithin3std)*100/len(weightlist)))

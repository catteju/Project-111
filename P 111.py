import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random
import pandas as pd

df = pd.read_csv("Data.csv")
data = df["readingTime"].tolist()

populationMean = s.mean(data)
print("Population Mean", populationMean)
populationStd = s.stdev(data)
print("Standard Deviation Of Population Mean", populationStd)

def randomSamples(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data))
        value = data[randomIndex]
        dataSet.append(value)
    mean = s.mean(dataSet)
    return mean

def showFigure(meanList):
    df = meanList
    fig1 = ff.create_distplot([df],["readingTime"], show_hist= False)
    fig1.show()

meanList = []
for i in range(0,100):
    setOfMeans = randomSamples(30)
    meanList.append(setOfMeans)
showFigure(meanList)
mean = s.mean(meanList)
print("Sampling Mean",s.mean(meanList))
std = s.stdev(meanList)
print("Standard Deviation Of Sampling Distribution", std)


first_std_start, first_std_end = mean - std, mean + std 
second_std_start, second_std_end = mean - (2*std), mean + (2*std)
third_std_start, third_std_end = mean - (3*std), mean + (3*std)

newDataSet = []
for i in range(0, 100):
    randomIndex = random.randint(0, len(data))
    value = data[randomIndex]
    newDataSet.append(value)
newSampleMean = s.mean(newDataSet)

fig = ff.create_distplot([meanList],["readingTime"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,2], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [newSampleMean,newSampleMean], y = [0,2], mode = "lines", name = "Intervention MEAN"))
fig.add_trace(go.Scatter(x = [first_std_start, first_std_start], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [second_std_start, second_std_start], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [third_std_start, third_std_start], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 3"))

fig.show()
zScore = (mean - newSampleMean)/std
print("Z-Score = ",zScore)
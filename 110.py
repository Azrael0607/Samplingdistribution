import csv 
import plotly.figure_factory as ff
import pandas as pd 
import statistics
import random

from scipy.__config__ import show
df = pd.read_csv('data.csv')
data = df['temp'].tolist()
#fig = ff.create_distplot([data],['temp'],show_hist= False)
#fig.show()

population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print('population mean is ',population_mean)
print('standard deviation of whole data is ', std_deviation)
def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean1 = statistics.mean(dataset)
    std_deviation1 = statistics.stdev(dataset)
    print('mean of sample is', mean1)
    print('std deviation of sample is ',std_deviation1)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['temp'],show_hist= False)
    fig.show()

def setup():
    mean_list = []
    for i in range (1,1000):
        set_of_means = randomsetofmean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()

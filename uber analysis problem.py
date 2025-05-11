# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read files
dataset = pd.read_csv("C:\\Users\\user\\Downloads\\UberDataset.csv")
# information of data
table = dataset.info

Head = dataset.head()
# check null cells
print(data.isnull().sum())

# Data cleaning
dataset["PURPOSE"].fillna("Not")
# it filled the empty cells with Not
dataset["START_DATE"] = pd.to_datetime(dataset["START_DATE"], errors='coerce')
# convert the datatype of this column into datetime datatype
dataset["END_DATE"] = pd.to_datetime(dataset["END_DATE"], errors='coerce')
# convert the datatype of this column into datetime datatype
dataset["date"] = pd.DatetimeIndex(dataset["START_DATE"]).date
# creating new column date
dataset["time"] = pd.DatetimeIndex(dataset["START_DATE"]).hour
# creating new column  time
Range = [0, 10, 15, 19, 24]
heading = ["Morning", "Evening", "Afternoon", "Night"]
dataset["period"] = pd.cut(x=dataset["time"], bins=Range, labels=heading, right=False)
# creating new column period and using range
dataset.dropna(inplace=True)
# removing null and empty cells

# data visualization
plt.figure(figsize=(20, 5))

plt.subplot(1, 2, 1)
Figure1 = sns.countplot(x=dataset["CATEGORY"])
plt.show()

# use sns count plot function for draw the graph on the bases of category
figure2 = sns.countplot(x=dataset["PURPOSE"])
plt.show()

# sns count plot function is counting the no. of common values in column and put in the graph
figure3 = sns.countplot(x=dataset["period"])
plt.show()

# graph on period column
dataset["month"] = pd.DatetimeIndex(dataset["date"]).month
# month column and its elements i 1,2,3,4 ect.
month_d ={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
# dictionary for month store key as num and value as name of month
dataset["month"] = dataset.month.map(month_d)
# map function for containing column month with dictionary month_d
month_count = dataset.month.value_counts(sort=False)
# it counts the total no. jan, feb, mar upto dec.
data = {'Month': month_count.values, 'count value': dataset.groupby('month', sort=False)["MILES"].max()}
df = pd.DataFrame(data).reset_index()
# data frame where month store total no. of times month repeated and count value store the maximum miles of the month
sns.lineplot(data=df,  x='month', y='count value')
plt.show()
dataset["day"] = dataset.START_DATE.dt.weekday
# column contain numbers such 0,1,2,3,4,5 and 6
day_dis = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
# dictionary where key id no. and value is name of days like mon
dataset["day"] = dataset["day"].map(day_dis)
# map column with dictionary
day_count = dataset.day.value_counts(sort=False)
# count the total no. of time days repeated
sns.barplot(x=day_count.index, y=day_count)
plt.show()

sns.boxplot(dataset["MILES"])
plt.show()

sns.boxplot(dataset[dataset["MILES"] < 100]["MILES"])
plt.show()

sns.boxplot(dataset[dataset["MILES"] < 40]["MILES"])
plt.show()

sns.boxplot(dataset[dataset["MILES"] < 30]["MILES"])
plt.show()

sns.displot(dataset[dataset["MILES"] < 30]["MILES"])
plt.show()


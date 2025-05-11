# <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png" alt="Uber Logo" width="100"/>  Data Analysis

## 📘 Project Overview

This project involves analyzing Uber data from START DAT, END DATE, CATEGORY, START, STOP, MILES, PURPOSE, date, time and  period. The analysis encompasses data cleaning, feature engineering, and visualization to understand Uber data patterns and trends.

## 📂 Dataset Description
- Data Sources: CSV files for each city containing air quality measurements.

- Parameters: CATEGORY, START, STOP, MILES, PURPOSE

- Time Frame: Data spans from 2020 to 2024.

- Timestamp: Each record includes a timestamp indicating the date of measurement.

## 🧹 Data Cleaning and Preprocessing
##  import fiels from  
```python
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
```
##  Read all fiels
```python
 dataset = pd.read_csv("C:\\Users\\user\\Downloads\\UberDataset.csv")

```

## 4) Information about data
```python
print(dataset.info())
print(dataset.head())
print(dataset.describe())
```
##  Checking null cells and duplicated cells
```python
print(dataset.isnull().sum())
print(dataset.duplicated().sum())
```

##  Fill null cells
```pythondataset["PURPOSE"].fillna("Not")
```

## 7) Categorizing and Converting columns data type:

Create categorical ranges for pollutants to assess air quality levels:
```python
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
```
### Remove empty cells
```python
dataset.dropna(inplace=True)
# removing null and empty cells
```
## Data Visualization

##  Categories Baised Graph :

Count plots for each  category:
```python
plt.figure(figsize=(20, 5))

plt.subplot(1, 2, 1)
Figure1 = sns.countplot(x=dataset["CATEGORY"])
plt.show()
# use sns count plot function for draw the graph on the bases of category

```

## 9) Purpose Based Graph:

Count plots showing Purpose data Distribution:
```python
figure2 = sns.countplot(x=dataset["PURPOSE"])

plt.show()
# sns count plot function is counting the no. of common values in column and put in the graph
```

##  Period Based Graph:

Count Plot showing Period:
```python
figure3 = sns.countplot(x=dataset["period"])
plt.show()
# graph on period column
```
##  Monthly Based Graph:

Line plots showing Monthly max miles data:
```python
dataset["month"] = pd.DatetimeIndex(dataset["date"]).month
# month column and its elements i 1,2,3,4 ect.
month_d ={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
# dictionary for month store key as num and value as name of month
dataset["month"] = dataset.month.map(month_d)
# map function for containing column month with dictionary month_d
month_count = dataset.month.value_counts(sort=False)
# it counts the total no. jan, feb, mar upto dec.
df = pd.DataFrame({'Month': month_count.values, 'count value': dataset.groupby('month', sort=False)["MILES"].max()})
# data frame where month store total no. of times month repeated and count value store the maximum miles of the month
sns.lineplot(data=df,  x='Month', y='count value')

plt.show()
```

##  Weekdays Based Graph:

Bar plots showing Weekdays  data:
```python
dataset["month"] = pd.DatetimeIndex(dataset["date"]).month
# month column and its elements i 1,2,3,4 ect.
month_d ={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
# dictionary for month store key as num and value as name of month
dataset["month"] = dataset.month.map(month_d)
# map function for containing column month with dictionary month_d
month_count = dataset.month.value_counts(sort=False)
# it counts the total no. jan, feb, mar upto dec.
data = {'Month': month_count.values,'count value': dataset.groupby('month', sort=False)["MILES"].max()}
df = pd.DataFrame(data).reset_index()
# data frame where month store total no. of times month repeated and count value store the maximum miles of the month
print(df.Month, df['count value'])
print(df)
sns.lineplot(data=df,  x='month', y='count value')
plt.show()

```

##  Average Miles Covery By Customer:

Box and Dis plots showing Average  miles per Customer data:
```python
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

```
## 📈 Key Insights
- Most customers used the Business category when booking Uber rides.

- The primary purpose of travel was for Meetings.

- The Evening was the most common time period for Uber usage.

- March to April was the peak period for ride bookings.

- Saturday had the lowest number of Uber rides.

- The average distance traveled by customers was approximately 25 miles.

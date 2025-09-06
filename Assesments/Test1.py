"""VaishnaviGajinkar_A15_Test1.ipynb
# Section A

Q1 Solution 1


=SUMIF(Table1[Region], "North",Table1[Sales])
"""
"""The data is saved as a table named Table1. Values from Sales column is added only if Region has a value of 'North'

Q1 Solution 2

Create a table out of the data using ctrl+T.
Create a pivot table using the Insert tab in ribbon.
Drag the 'Regions' column in Rows field
         'Products' in Column field
         and 'Sales' in Values field.
Make sure the aggregation of values field is set to SUM

Q1 Solution 3

Using the filters of the table, select the non-blanks of Sales column.
Using the bottom ribbon, check the average value of the Sales column data.
Now keep only blanks selected in Sales col. Enter the average value as seen before.

Q2 Solution 1
"""

import pandas as pd
data = {
 'Employee': ['A','B','C','D','E'],
 'Department': ['HR','Finance','Finance','HR','IT'],
 'Salary': [50000, 60000, None, 52000, 70000]
}
df = pd.DataFrame(data)
avgSal = df.groupby('Department')['Salary'].mean()                                  # avg salary in each dept
print(avgSal)


"""Q2 Solution 2"""

import pandas as pd
data = {
 'Employee': ['A','B','C','D','E'],
 'Department': ['HR','Finance','Finance','HR','IT'],
 'Salary': [50000, 60000, None, 52000, 70000]
}
df = pd.DataFrame(data)

print(df['Employee'][df['Salary']==df['Salary'].max()])                             #  employee with the maximum salary 

"""Q2 Solution 3

Since the other values of dataset have low variance, the missing value can be imputed with departmental average. The department of Finance has 2 values, hence replacing with 0 is not better. Dropping the value is the last option as it leads to loss of data.

Q3 Solution 1

SELECT CustomerID, SUM(Amount) FROM Orders GROUP BY CustomerID

Q3 Solution 2

SELECT CustomerID, SUM(Amount) as Total FROM Orders GROUP BY CustomerID ORDER BY Total DESC LIMIT 2

Q3 Solution 3

SQL result will not be affected because of Null values, hence it can be ignored. However filtering the results with a WHERE clause can be opted.

Q4 Solution 1
"""

import numpy as np
temps = np.array([30, 32, 28, 31, 29, 35, 33])

avg = np.mean(temps)
medn = np.median(temps)
stdiv = np.std(temps)

print("Average", avg)
print("Median", medn)
print("Std Div", stdiv)

"""Q4 Solution 2"""

import numpy as np
temps = np.array([30, 32, 28, 31, 29, 35, 33])

avg = np.mean(temps)
medn = np.median(temps)
stdiv = np.std(temps)

print(temps[temps>np.mean(temps)])
count = len(temps[temps>np.mean(temps)])
print(count)

"""Q4 Solution 3

Since NAN values affect the average, the np.nan_to_num(data, nan=value) function can be used to replace all nan fields with the value

# Section B

Q5 Solution 1

From the data it is clear that product B shows consistent growth from Jan to Feb

Q5 Solution 2
"""

=

"""Q5 Solution 3

Q6 Solution 1
"""

import pandas as pd
import numpy as np
data = {
 'CustomerID': ['C1','C2','C3','C4'],
 'Tenure': [12,5,3,20],
 'MonthlyCharges': [1000,700,1200,800],
 'Churn':['Yes','No','Yes','No']
}
df = pd.DataFrame(data)

churn_yes = np.where(df['Churn'] =='Yes', df['MonthlyCharges'].mean(), data['Churn'])
churn_no = np.where(df['Churn'] =='No', df['MonthlyCharges'].mean(), data['Churn'])
print(churn_yes)
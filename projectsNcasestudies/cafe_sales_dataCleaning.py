import numpy as np
import pandas as pd

data = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\Python\CodingWise\projectsNcasestudies\cafe_sales (messy_data).csv')

print(data.head())                                      # displays content of dataset

print(data.isnull().sum())                              # checking missing values in each column

print(data['Quantity'].dtype)
# data.astype(float)
data['Quantity'].fillna(data['Quantity'].mean(),inplace=True)            # fill the blanks with average values of other rows
data['Price Per Unit'].fillna(data['Price Per Unit'].median(),inplace=True)            # fill the blanks with median values of other rows

data.replace([np.inf, -np.inf], np.nan, inplace=True)                 # replace all infinites with NAN value
# print(data.isnull().sum())

data.dropna(inplace=True)                                # drop all rows having NA cells in the dataset 

print("Shape of dataset with duplicates",data.shape)
data.drop_duplicates(inplace=True)                                  # drops all duplicate values at all column level
print("Shape of dataset without duplicates",data.shape)

data['Total Spent'] = np.where(data['Total Spent'] < 0, data['Total Spent'].mean(), data['Total Spent'])    # replacing negative values of col with average of current non-negative col value

# replace outlier values by 

avg_spend = data['Total Spent'].mean()
spend_stdiv = data['Total Spent'].std()
lower_bound = avg_spend - (3 * spend_stdiv)
upper_bound = avg_spend + (3 * spend_stdiv)

df = data[(data['Total Spent']>= lower_bound) & (data['Total Spent']<= upper_bound)]          # defining acceptable range (i.e. removing rows having too high or too low values)
print(df)

print(df.isnull().sum())                              # checking missing values in each column

print("Final shape of dataset after cleaning",df.shape)

df.to_csv('cafe_sales (clean_data).csv', index=False)

print("Data cleaning complete !")

'''
OUTPUT : 
Transaction ID    Item  Quantity  Price Per Unit  Total Spent  Payment Method  Location Transaction Date
0    TXN_1961373  Coffee       2.0             2.0          4.0     Credit Card  Takeaway         9/8/2023
1    TXN_4977031    Cake       4.0             3.0         12.0            Cash  In-store        5/16/2023
2    TXN_4271903  Cookie       4.0             1.0          NaN     Credit Card  In-store        7/19/2023
3    TXN_7034554   Salad       2.0             5.0         10.0         UNKNOWN   UNKNOWN        4/27/2023
4    TXN_3160411  Coffee       2.0             2.0          4.0  Digital Wallet  In-store        6/11/2023
Transaction ID         0
Item                 333
Quantity             483
Price Per Unit       164
Total Spent          331
Payment Method      2579
Location            3267
Transaction Date     159
dtype: int64
float64

Shape of dataset with duplicates (4530, 8)
Shape of dataset without duplicates (4530, 8)
     Transaction ID      Item  Quantity  Price Per Unit  Total Spent  Payment Method  Location Transaction Date
0       TXN_1961373    Coffee       2.0             2.0          4.0     Credit Card  Takeaway         9/8/2023
1       TXN_4977031      Cake       4.0             3.0         12.0            Cash  In-store        5/16/2023
3       TXN_7034554     Salad       2.0             5.0         10.0         UNKNOWN   UNKNOWN        4/27/2023
4       TXN_3160411    Coffee       2.0             2.0          4.0  Digital Wallet  In-store        6/11/2023
6       TXN_4433211   UNKNOWN       3.0             3.0          9.0           ERROR  Takeaway        10/6/2023
...             ...       ...       ...             ...          ...             ...       ...              ...
9979    TXN_9933628  Smoothie       5.0             4.0         20.0            Cash  In-store        7/20/2023
9986    TXN_2858441  Sandwich       2.0             4.0          8.0     Credit Card  In-store       12/14/2023
9991    TXN_3897619  Sandwich       3.0             4.0         12.0            Cash  Takeaway        2/24/2023
9992    TXN_2739140  Smoothie       4.0             4.0         16.0         UNKNOWN  In-store         7/5/2023
9999    TXN_6170729  Sandwich       3.0             4.0         12.0            Cash  In-store        11/7/2023

[4423 rows x 8 columns]
Transaction ID      0
Item                0
Quantity            0
Price Per Unit      0
Total Spent         0
Payment Method      0
Location            0
Transaction Date    0
dtype: int64
Final shape of dataset after cleaning (4423, 8)
'''
import numpy as np
import pandas as pd

data = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\Python\CodingWise\projectsNcasestudies\Employee.csv')

print(data.head())                                      # displays content of dataset

print(data.isnull().sum())                              # checking missing values in each column

data['ExperienceInCurrentDomain'].fillna(data['ExperienceInCurrentDomain'].mean())            # fill the blanks with average experience of all emps

data.replace([np.inf, -np.inf], np.nan)                 # detect all infinite & NAN values

data.fillna(data.mean())                                # fill the NA cells with mean value of that column

data.drop_duplicates()                                  # drops all duplicate values at all column level
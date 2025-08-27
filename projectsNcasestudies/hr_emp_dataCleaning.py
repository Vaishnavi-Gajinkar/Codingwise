import pandas as pd

#-------------Reading dataset-------------

data = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\Python\CodingWise\projectsNcasestudies\hr_emp_data.csv')
df = pd.DataFrame(data)
print(df.head())                                                                            # viewing top 5 rows of data set

#-------------Understanding dataset-------------

print("\nInformation regarding data")
df.info()                                                                                   # summary of all columns of data set

print("\nShape of dataset")
print(df.shape)

print("\nColumns of dataset")
print(df.columns)

print("\n Count of blanks in each column of dataset")
print(df.isnull().sum())

# -----------Cleaning Dataset--------------

df['PerformanceRating'].fillna(1, inplace=True)                                                          
df['Age'].fillna(df['Age'].mean(), inplace=True)                                            # filling blank values with an aggregated value
df['PercentSalaryHike'].fillna(df['PercentSalaryHike'].median(), inplace=True)

df['Over18'] = df['Over18'].fillna('Y', inplace=True)

df['EmployeeNumber'] = df['EmployeeNumber'].interpolate(method='linear', inplace=True)      # interpolating data

# df.dropna(axis=0, inplace=True)

#-------------Modifying dataset-------------

df['CTC'] = df['MonthlyIncome'] * 12                                                        # adding new column

# df.drop(columns=['EmployeeCount, StandardHours','StockOptionLevel'], inplace=True)          # dropping unnecessary columns

print("\nSorting dataset based on decreasing 'HourlyRate'")                                 # sorting dataset based on single column
print(df.sort_values('HourlyRate', ascending=False, inplace=True))

print("\nTotal Expense to the company:", df['CTC'].sum())                                   # aggregating columns of dataset
print("\nTotal employees working in company:", df['EmployeeNumber'].count())
print("\nAverage percent salary hike:", df['PercentSalaryHike'].mean())
print("\nDistance of emp staying nearest to office:", df['DistanceFromHome'].min(), "km(s)")
print("\nMax years an emp has worked here:", df['YearsAtCompany'].max())

print("\nAverage emp age as per education field and maritial status")
print(df.groupby(['EducationField','MaritalStatus'])['Age'].mean())                         # grouping dataset based on multiple columns

#---------------Saving the cleaned data-------------------

print(df.isnull().sum())
print(df.describe())
df.to_csv("hr_emp (clean_data).csv", index=False)
print("Data cleaning completed!")

'''
OUTPUT :
    Age Attrition     BusinessTravel  DailyRate              Department  DistanceFromHome  ...  TrainingTimesLastYear WorkLifeBalance  YearsAtCompany  YearsInCurrentRole  YearsSinceLastPromotion YearsWithCurrManager
0  41.0       Yes      Travel_Rarely       1102                   Sales                 1  ...                      0               1               6                   4                        0                    5
1  49.0        No  Travel_Frequently        279  Research & Development                 8  ...                      3               3              10                   7                        1                    7
2  37.0       Yes      Travel_Rarely       1373  Research & Development                 2  ...                      3               3               0                   0                        0                    0
3  33.0        No  Travel_Frequently       1392  Research & Development                 3  ...                      3               3               8                   7                        3                    0
4  27.0        No      Travel_Rarely        591  Research & Development                 2  ...                      3               3               2                   2                        2                    2

[5 rows x 35 columns]

Information regarding data
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1470 entries, 0 to 1469
Data columns (total 35 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Age                       1457 non-null   float64
 1   Attrition                 1464 non-null   object 
 2   BusinessTravel            1470 non-null   object 
 3   DailyRate                 1470 non-null   int64
 4   Department                1470 non-null   object
 5   DistanceFromHome          1470 non-null   int64
 6   Education                 1470 non-null   int64
 7   EducationField            1470 non-null   object
 8   EmployeeCount             1470 non-null   int64
 9   EmployeeNumber            1320 non-null   float64
 10  EnvironmentSatisfaction   1470 non-null   int64
 11  Gender                    1470 non-null   object
 12  HourlyRate                1470 non-null   int64
 13  JobInvolvement            1470 non-null   int64
 14  JobLevel                  1470 non-null   int64
 15  JobRole                   1470 non-null   object
 16  JobSatisfaction           1470 non-null   int64
 17  MaritalStatus             1470 non-null   object
 18  MonthlyIncome             1470 non-null   int64
 19  MonthlyRate               1470 non-null   int64
 20  NumCompaniesWorked        1470 non-null   int64
 21  Over18                    1464 non-null   object
 22  OverTime                  1470 non-null   object
 23  PercentSalaryHike         1460 non-null   float64
 24  PerformanceRating         1463 non-null   float64
 25  RelationshipSatisfaction  1470 non-null   int64
 26  StandardHours             1470 non-null   int64
 27  StockOptionLevel          1470 non-null   int64
 28  TotalWorkingYears         1470 non-null   int64
 29  TrainingTimesLastYear     1470 non-null   int64
 30  WorkLifeBalance           1470 non-null   int64
 31  YearsAtCompany            1470 non-null   int64
 32  YearsInCurrentRole        1470 non-null   int64
 33  YearsSinceLastPromotion   1470 non-null   int64
 34  YearsWithCurrManager      1470 non-null   int64
dtypes: float64(4), int64(22), object(9)
memory usage: 402.1+ KB

Shape of dataset
(1470, 35)

Columns of dataset
Index(['Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department',
       'DistanceFromHome', 'Education', 'EducationField', 'EmployeeCount',
       'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
       'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
       'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
       'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',
       'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
       'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager'],
      dtype='object')

 Count of blanks in each column of dataset
Age                          13
Attrition                     6
BusinessTravel                0
DailyRate                     0
Department                    0
DistanceFromHome              0
Education                     0
EducationField                0
EmployeeCount                 0
EmployeeNumber              150
EnvironmentSatisfaction       0
Gender                        0
HourlyRate                    0
JobInvolvement                0
JobLevel                      0
JobRole                       0
JobSatisfaction               0
MaritalStatus                 0
MonthlyIncome                 0
MonthlyRate                   0
NumCompaniesWorked            0
Over18                        6
OverTime                      0
PercentSalaryHike            10
PerformanceRating             7
RelationshipSatisfaction      0
StandardHours                 0
StockOptionLevel              0
TotalWorkingYears             0
TrainingTimesLastYear         0
WorkLifeBalance               0
YearsAtCompany                0
YearsInCurrentRole            0
YearsSinceLastPromotion       0
YearsWithCurrManager          0
dtype: int64

Total Expense to the company: 114711708

Total employees working in company: 0

Average percent salary hike: 15.191156462585035

Distance of emp staying nearest to office: 1 km(s)

Max years an emp has worked here: 40

Average emp age as per education field and maritial status
EducationField    MaritalStatus
Human Resources   Divorced         34.571429
                  Married          37.111111
                  Single           45.000000
Life Sciences     Divorced         37.446624
                  Married          37.401090
                  Single           36.566406
Marketing         Divorced         37.174230
                  Married          39.674335
                  Single           35.750000
Medical           Divorced         38.056075
                  Married          37.776190
                  Single           34.393521
Other             Divorced         35.947368
                  Married          36.250000
                  Single           33.777778
Technical Degree  Divorced         37.730769
                  Married          38.065574
                  Single           32.798307
Name: Age, dtype: float64
Age                            0
Attrition                      6
BusinessTravel                 0
DailyRate                      0
Department                     0
DistanceFromHome               0
Education                      0
EducationField                 0
EmployeeCount                  0
EmployeeNumber              1470
EnvironmentSatisfaction        0
Gender                         0
HourlyRate                     0
JobInvolvement                 0
JobLevel                       0
JobRole                        0
JobSatisfaction                0
MaritalStatus                  0
MonthlyIncome                  0
MonthlyRate                    0
NumCompaniesWorked             0
Over18                      1470
OverTime                       0
PercentSalaryHike              0
PerformanceRating              0
RelationshipSatisfaction       0
StandardHours                  0
StockOptionLevel               0
TotalWorkingYears              0
TrainingTimesLastYear          0
WorkLifeBalance                0
YearsAtCompany                 0
YearsInCurrentRole             0
YearsSinceLastPromotion        0
YearsWithCurrManager           0
CTC                            0
dtype: int64
               Age    DailyRate  DistanceFromHome    Education  EmployeeCount  EnvironmentSatisfaction  ...  WorkLifeBalance  YearsAtCompany  YearsInCurrentRole  YearsSinceLastPromotion  YearsWithCurrManager            CTC
count  1470.000000  1470.000000       1470.000000  1470.000000         1470.0              1470.000000  ...      1470.000000     1470.000000         1470.000000              1470.000000           1470.000000    1470.000000
mean     36.923816   802.485714          9.192517     2.912925            1.0                 2.721769  ...         2.761224        7.008163            4.229252                 2.187755              4.123129   78035.175510
std       9.071779   403.509100          8.106864     1.024165            0.0                 1.093082  ...         0.706476        6.126525            3.623137                 3.222430              3.568136   56495.481397
min      18.000000   102.000000          1.000000     1.000000            1.0                 1.000000  ...         1.000000        0.000000            0.000000                 0.000000              0.000000   12108.000000
25%      30.000000   465.000000          2.000000     2.000000            1.0                 2.000000  ...         2.000000        3.000000            2.000000                 0.000000              2.000000   34932.000000
50%      36.000000   802.000000          7.000000     3.000000            1.0                 3.000000  ...         3.000000        5.000000            3.000000                 1.000000              3.000000   59028.000000
75%      43.000000  1157.000000         14.000000     4.000000            1.0                 4.000000  ...         3.000000        9.000000            7.000000                 3.000000              7.000000  100548.000000
max      60.000000  1499.000000         29.000000     5.000000            1.0                 4.000000  ...         4.000000       40.000000           18.000000                15.000000             17.000000  239988.000000

[8 rows x 26 columns]
Data cleaning completed!
'''
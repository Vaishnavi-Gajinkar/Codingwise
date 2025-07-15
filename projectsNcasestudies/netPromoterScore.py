''' CASE STUDY - NET PROMOTER SCORE
a.k.a. Likelyhood To Recommend Survey
NPS helps a brand in gauging its brand value and sentiment in the market.
Promoters are highly likely to recommend your product or sevice. Hence, bringing in more business.
whereas, Detractors are likely to recommend against your product or service's usage. Hence, bringing the business down.
These insights can help business make customer oriented decision along product improvisation.
Widely used by companies and service providers to evaluate their performance & customer satisfaction.
2/3 of Fortune 500 companies use NPS
    How is the overall experience for them?
    What are some things that they like?
    What do they don't like?
Based on the feedback received, sometimes we end up getting really good insights, and tackle them.
This will help improve the next month's NPS.
Responses are given a scale ranging from 0-10, with 0 labeled with "Not at all likely," and 10 labeled with "Extremely likely."
'''
# NPS = % Promoters - % Detractors
# range of NPS: [-100, 100]

import numpy as np

data = np.loadtxt(r'C:\Users\Lenovo\OneDrive\Documents\Python\Notes\Python All Lecture Notes and Datasets\NPSsurvey.txt',dtype='int')

print(data)

print('\n',data.dtype)

print('\n',data.shape)

detractors = data[data<7]

print('\n',detractors)

promoters = data[data>=9]

print('\n',promoters)

per_promoters = promoters.shape[0] / data.shape[0] * 100

print('\n',f'Promoters = {per_promoters}%')

per_detractors = detractors.shape[0] / data.shape[0] * 100

print('\n',f'Detractors = {per_detractors}%')

NPS = per_promoters - per_detractors

print('\n',f'NPS of this dataset is {NPS}')

'''
OUTPUT :
[8 2 5 ... 1 2 7]

int64

(1167,)

[2 5 4 2 5 6 1 5 1 6 5 3 3 3 2 6 6 1 4 2 4 4 1 5 3 1 4 2 2 5 5 1 4 4 1 2 3
 6 6 1 2 6 1 3 5 6 3 5 1 3 4 3 3 6 1 3 1 2 3 2 3 4 5 2 4 4 5 3 1 4 3 6 6 6
 2 1 5 1 5 5 1 5 3 3 5 4 1 4 1 1 6 6 4 5 5 1 2 1 4 4 5 1 6 3 1 3 1 2 4 6 2
 4 2 3 6 3 4 1 3 4 6 3 5 5 3 2 2 6 4 1 5 5 3 4 6 5 6 3 1 2 4 5 2 2 5 1 1 5
 2 3 5 1 2 5 2 2 3 6 6 5 5 5 6 4 5 4 2 2 3 3 2 6 3 1 3 3 5 1 3 3 2 3 4 5 3
 5 6 5 5 3 3 5 6 2 2 6 6 2 3 5 5 1 2 2 3 5 2 1 3 2 1 4 2 4 5 3 4 4 5 4 3 5
 1 3 1 1 5 2 2 3 4 5 3 1 5 6 1 2 3 2 3 4 6 3 5 1 2 6 5 6 5 2 2 1 5 6 5 1 3
 3 4 6 1 1 3 1 2 2 4 1 1 2 2 4 6 6 2 5 2 4 1 1 5 6 3 1 5 1 6 6 6 5 2 1 5 6
 6 2 1 6 2 3 5 5 5 5 4 2 1 6 3 3 5 2 2 1 4 1 6 2 1 2 1 1 3 6 2 1 5 5 6 5 2
 1 5 4 1 4 4 4 5 3 2 2 3 3 2 1 1 2 6 5 5 4 2 2 1 1 3 3 2 1 1 5 2 2 1 5 2 3
 1 4 2 6 5 3 4 6 1 5 2 4 1 4 4 4 3 6 3 3 1 5 5 4 1 4 5 4 5 5 2 3 5 1 4 1 4
 3 4 2 3 4 5 4 2 4 6 2 3 6 3 1 1 5 3 3 4 3 3 2 2 4 5 6 4 2 2 3 3 5 2 3 5 3
 1 6 1 6 4 2 1 1 4 3 5 6 5 3 6 2 1 6 2 6 1 3 4 6 6 4 1 6 4 3 3 6 2 5 6 6 1
 5 1 2 2 5 1 4 1 4 6 3 4 2 6 4 4 4 6 3 1 3 5 4 2 5 4 5 3 3 4 6 6 5 2 1 6 1
 2 5 2 4 2 5 4 4 1 6 5 5 5 3 3 3 6 6 1 3 3 3 4 6 5 1 4 4 6 2 1 2 3 5 2 5 5
 2 3 4 3 2 2 3 3 2 5 3 5 5 5 1 5 4 4 4 4 1 2 1 4 5 3 6 1 6 2 4 1 5 5 3 4 5
 5 5 3 3 4 5 5 5 5 4 4 6 5 5 2 2 4 3 5 6 1 2 2 1 3 1 5 1 6 3 4 1 4 5 6 2 4
 5 2 2 5 1 4 5 3 6 5 2 4 5 6 6 1 6 3 5 2 4 1 2 5 6 1 1 3 4 5 1 3 3 3 4 5 1
 2 3 2 2 5 1 5 6 3 6 5 4 4 3 2 2 5 1 5 5 2 5 5 4 4 1 3 6 5 2 1 1 4 1 5 2 6
 1 1 2 5 1 2]

[ 9 10  9  9 10  9 10 10  9  9  9  9 10 10  9  9 10 10  9 10  9  9 10 10
  9 10  9 10  9  9  9  9  9  9  9  9  9  9 10 10  9 10 10  9  9 10 10  9
 10 10  9 10 10  9  9  9  9  9  9  9  9  9 10 10  9  9 10 10  9 10 10 10
 10 10 10  9  9  9  9  9 10 10 10 10  9  9 10  9  9 10 10 10 10 10 10  9
  9 10 10  9  9 10  9 10 10  9  9 10 10 10  9  9  9 10  9  9  9  9  9  9
 10 10 10 10 10  9  9  9  9  9 10 10 10  9 10  9  9  9  9 10 10  9 10  9
 10  9  9 10  9  9 10  9  9  9 10  9 10  9 10  9  9 10 10  9 10 10 10  9
  9  9 10  9 10 10  9  9  9  9 10 10 10 10  9  9  9  9  9  9  9 10 10  9
 10 10 10 10 10  9  9 10  9  9  9  9 10  9 10 10  9  9  9  9 10  9 10  9
  9  9 10  9 10 10  9  9]

Promoters = 19.194515852613538%

Detractors = 60.75407026563839%

NPS of this dataset is -41.559554413024856
'''
orgDict = {
    'name':'Chandu', 'age': 25, 'salary': 30000
}
print(orgDict)
copyDict = orgDict.copy()
print(copyDict)
copyDict['gender']='M'
print(orgDict)
print(copyDict)
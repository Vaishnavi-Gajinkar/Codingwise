''' wap that handles AttributeError when calling a non-existent method '''



def existing_function(variable):
    ''' defining an existing function '''
    return 'Inside existing function'
    

try:
    print("Inside try block")
    string = existing_function('a').attribute

except AttributeError as e:
    print('Attribute error found',e)

finally:
    print('Inside finally block')

# Output:
'''
Inside try block
Attribute error found 'str' object has no attribute 'attribute'
Inside finally block
'''
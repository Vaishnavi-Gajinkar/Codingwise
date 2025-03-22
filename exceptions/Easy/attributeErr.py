''' wap that handles AttributeError when calling a non-existent method '''


class fun_class(object):
    class_variable = 12345
    def existing_function(parameter):
        ''' defining an existing function '''
        return 'Inside existing function'
    

try:
    print("Inside try block")
    print(fun_class.class_variable)
    print(fun_class.existing_function('a').attribute)

except AttributeError as e:
    print('Attribute error found,',e)

finally:
    print('Inside finally block')

# Output:
'''
Inside try block
Attribute error found 'str' object has no attribute 'attribute'
Inside finally block
'''
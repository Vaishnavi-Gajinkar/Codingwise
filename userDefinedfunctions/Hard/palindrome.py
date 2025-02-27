'''check if a string is a palindrome '''

def palin(sent):
    '''check if the passed string is a palindrome or not'''
    org_str = sent
    rev_str = sent[::-1]

    if org_str == rev_str:
        return f'Entered string is a palindrome'
    else:
        return f'Entered string is not a palindrome'
    
sentence = input("Enter a string (to check palindrome) ")

print(palin(sentence))
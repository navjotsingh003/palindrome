nav = input('Enter name: ')
nav1 = str(nav)                 #we are changing the variable to string
if nav1 == nav1[::-1]:
    print('It is palindrome')
else:
    print('It is not palindrome')

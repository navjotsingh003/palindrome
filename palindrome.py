nav = input('Enter name: ')
nav1 = str(nav)
if nav1 == nav1[::-1]:
    print('It is palindrome')
else:
    print('It is not palindrome')
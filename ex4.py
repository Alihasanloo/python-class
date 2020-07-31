""" 012 """
"""
I=int(input('Enter the first number: '))
II=int(input('Enter the second number: '))
if I>II:
    print(II,I)
else:
    print(I,II)
print(' ***DONE*** ')
"""
""" 013 """
"""
n=int(input(' Please enter a number under 20: '))
if n>=20:
    print(' the entered number is too high ')
else:
    print(' Thank you')
"""
""" 014 """
"""
n=int(input(' Please enter a number between 10 and 20: '))
if n<20 and n>10:
    print(' Thank you ')
else:
    print(' Wrong Entry')    
"""
""" 015 """
"""
C=str(input('what is your favorite color? '))
if C in ['Red','RED','red']:
    print('I like Red too! :) ')
else:
    print('I do not like ',C,' ','I prefer Red!')

"""
""" 016 """

w=str(input('Is it rainy out there? (yes/No) '))
w=w.lower()
if w in ['yes','y','yeah']:
    win=str(input('Is it windy out there? (yes/No) '))
    win=win.lower()
    if win in ['yes','y','yeah']:
        print('it is too windy for taking out an umbrella! ')
    elif win in ['no','n','nope']:
        print(' it is better to take an umbrella. ')
elif w in ['no','n','nope']:
    print('Enjoy your day! ')

""" 017 """
"""
a=int(input('How old are you? '))
if a>=18:
    print('you can vote! ')
elif a==17:
    print('you can learn to drive. ')
elif a==16:
    print('you can buy a lottery ticket')
else:
    print('Beshin Darsato Bekhun :)')
"""
"""018"""
"""
n=int(input('enter a number: '))
if n<10:
    print('Too Low')
elif n>=10 and n<=20:
    print('correct')
else:
    print('Too High')
restart_program()
"""
"""019"""
"""
n=int(input('enter a number 1 or 2 or 3: '))
if n==1:
    print('Thanks')
elif n==2:
    print('well done')
elif n==3:
    print('correct')
else:
    print('error')
"""

    

































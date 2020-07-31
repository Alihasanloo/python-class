"""
C=('Italy','Iran','France','Spain','England')
print(C)
a=str(input('choose one of the above countries:'))
a=a.lower()
a=a.capitalize()
if a in C:
    print(C.index(a))
else:
    print('wrong entry')
"""
"""
C=('Italy','Iran','France','Spain','England')
print(C)
a=int(input('enter a number from 0 to 4:'))
if a>=0 and a<=4:
    print(C[a])
else:
    print('wrong entry')
"""
"""
ls=['Football','Snooker']
s=str(input('What is your favorite sport? '))
ls.append(s)
ls.sort()
print(ls)
"""
"""
L=['eraser','pencil','pen','ink','stamp']
print(L)
d=str(input('which one of the above list dont you like?'))
d=d.lower()
if d in L:
    L.remove(d)
    print(L)
else:
    print('Try again')
"""


"""Leap Year Calculation"""
def lyc(Y,M,D):
    if Y % 4 != 0 or Y % 100 == 0 and Y % 400 != 0:
        L=0
    elif Y % 4 == 0:
        L=1
    LY=[31,29,31,30,31,30,31,31,30,31,30,31]
    NY=[31,28,31,30,31,30,31,31,30,31,30,31]
    if L==1:
        ms=sum(LY[:M-1])
        dn=ms+D
        print('the entered date is the',dn,'th day of the year')
    else:
        ms=sum(NY[:M-1])
        dn=ms+D
        print('the entered date is the',dn,'th day of the year')

Y=int(input(' Enter the Year Number: '))
M=int(input(' Enter the Month Number: '))
D=int(input(' Enter the Day Number: '))
r=lyc(Y,M,D)
print(r)

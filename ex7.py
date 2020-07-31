def fibo(sub):
    if sub==1:
        return 0
    elif sub==2:
        return 1
    else:
        return fibo(sub-2)+fibo(sub-1)
 
a=int(input('Enter the n value: '))
f=list(map(fibo,range(1,a+1)))
print(f)

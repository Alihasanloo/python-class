def fibo(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else:
        return fibo(a-2)+fibo(a-1)
    

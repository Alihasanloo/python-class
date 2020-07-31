def fibo(arg):
    if arg==1:
        return 0
    elif arg==2:
        return 1
    else:
        return fibo(arg-2)+fibo(arg-1)
    

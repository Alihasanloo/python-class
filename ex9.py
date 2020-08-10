class time:
    def __init__(arg,Hour,Minute,Second):
        arg.h=Hour
        arg.m=Minute
        arg.s=Second
        
    def show(arg):
        return str(arg.h)+':'+str(arg.m)+':'+str(arg.s)

    def __str__(arg):
        return str(arg.h)+':'+str(arg.m)+':'+str(arg.s)

    def __repr__(arg):
        return str(arg.h)+':'+str(arg.m)+':'+str(arg.s)

    def __add__(arg,other):
        if (arg.s + other.s)>= 60:
            arg.s-= 60
            arg.m += 1
        if (arg.m + other.m)> 60:
            arg.m -= 60
            arg.h += 1
        return arg.h + other.h, arg.m + other.m , arg.s + other.s

    def __sub__(arg,other):
        return arg.h - other.h, arg.m - other.m , arg.s - other.s

    def __gt__(arg,other):
        ssa=arg.s+(60*arg.m)+(3600*arg.h)
        sso=other.s+(60*other.m)+(3600*other.h)
        if ssa > sso:
            return "True"
        else:
            return "False"
    def __lt__(arg,other):
        ssa=arg.s+(60*arg.m)+(3600*arg.h)
        sso=other.s+(60*other.m)+(3600*other.h)
        if ssa < sso:
            return "True"
        else:
            return "False"

    def __eq__(arg,other):
        ssa=arg.s+(60*arg.m)+(3600*arg.h)
        sso=other.s+(60*other.m)+(3600*other.h)
        if ssa==sso:
            return "True"
        else:
            return "False"
    


"""
x_coordinate=int(input('enter the second:'))
y_coordinate=int(input('enter the minute:'))
z_coordinate=int(input('enter the hour:'))
setattr(t , 's' , sec)
setattr(t , 'm' , minute)
setattr(t , 'h' , hr) 

print(t.show())
"""

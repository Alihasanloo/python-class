year=int(input('Enter the year Number'))
if year % 4 !=0:
    print('none-Kabise :)')
elif year % 4 ==0 and year % 100 ==0:
    print('Kabise :)')
elif year % 4 ==0 and year % 100 !=0:
    print('None-Kabise :)')
elif year % 4 ==0:
    print('Kabise :)')
print('done')


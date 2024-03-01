intial=input().split()
subtractions=int(intial[1])
number=str(intial[0])
number_int_last=int(number[-1])
number_int=int(intial[0])
for i in range(subtractions):
    if number_int_last==0:
        number_int//=10
        number=str(number_int)
        number_int_last=int(number[-1])
    elif number_int_last!=0:
        number_int-=1
        number=str(number_int)
        number_int_last=int(number[-1])
print(number_int)

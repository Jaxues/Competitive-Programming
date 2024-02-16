num_one=list(map(str,input()))
num_two=list(map(str,input()))

final=list()
for (num1,num2) in zip(num_one,num_two):
    if num1>num2:
        final.append(num1)
    elif num2>num1:
        final.append(num2)
    if num1==num2:
        final.append("0")

print("".join(final))

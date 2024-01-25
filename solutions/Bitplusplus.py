num=int(input())
x=0
for i in range(num):
    operation=input()
    if operation.lower() == "++x" or operation.lower() =="x++":
        x+=1
    elif operation.lower() == "--x" or operation.lower() =="x--":
        x-=1
print(x)


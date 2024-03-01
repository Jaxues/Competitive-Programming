num=int(input())
fib={0,1,2,3,5,8,13}
string=[]
for i in range(1,num+1):
    if i in fib:
        string.append("fizz")
    elif i not in fib:
        string.append("buzz")
print("".join(string))

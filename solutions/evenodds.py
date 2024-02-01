num=list(map(int,input().split()))
even=list()
odds=list()
for i in range(1,num[0]+1):
    if i%2==0:
        even.append(i)
    else:
        odds.append(i)
value=num[1]
evenodds=odds+even
print(evenodds[value-1])

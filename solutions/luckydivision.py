num=int(input())
lucky={'7','4'}
lucky_count=0
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(str(i))
    

for factor in factors:
    temp_set=set()
    for string in factor: 
        temp_set.add(string)
    if temp_set.issubset(lucky):
        lucky_count=1
        break
    else:
        temp_set=set()

if lucky_count==1:
    print("YES")
else:
    print("NO")


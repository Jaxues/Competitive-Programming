# Exceeds timelimit on test case 8
num=list(map(int,input().split()))
range_num=num[0]
position=num[1]
evens=[]
odds=[]
for number in range(1,range_num+1):
    if number%2==0:
        evens.append(number)
    else:
        odds.append(number)
joined_list=odds+evens
print(joined_list[position-1])

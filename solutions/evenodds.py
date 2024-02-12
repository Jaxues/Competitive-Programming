num=list(map(int,input().split()))
range_num=num[0]
position=num[1]
if range_num==position:
    if range_num%2!=0:
        print(num[0]-1)
    else:
        print(num[0])
elif position/range_num <= 0.5:
    print(range_num//2)
else:
    print(2)

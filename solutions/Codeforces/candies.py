number=int(input())
number_candies=list(map(int,input().split()))
range_candies1,range_candies2 = map(int,input().split())
total_candies=0
for i in range(range_candies1,range_candies2+1):
    total_candies+=number_candies[i]
print(total_candies)

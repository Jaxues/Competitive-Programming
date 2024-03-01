num=int(input())

operations=[]
for i in range(num):
    entry=list(map(int,input().split()))
    operations.append(entry)

# loop through each element in the last of arrays.
# Find if operation is divisible by each other elese add one to total number of steps. Continue till gone through all elements
# Need to use module check if result of first divided by second element equals zero

intial=list(map(int,input().split()))
max_height=intial[1]
road=0
heights=list(map(int,input().split()))
for height in heights:
    if height>max_height:
        road+=2
    else:
        road+=1

print(road)

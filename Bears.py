bear1,bear2=map(int,input().split())
years=0
x=1
while x==1:
    years+=1
    bear1*=3
    bear2*=2
    if bear1>bear2:
        x=0

print(years)

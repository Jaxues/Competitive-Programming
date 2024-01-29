intial = list(map(int, input().split()))
money = intial[1]
bananas = intial[2]
cost = intial[0]
loan = 0
for i in range(0, bananas):
    spent=money-cost*(i+1)
    if spent>0:
        money-=cost*(i+1)
    elif spent<0 and loan==0:
        loan+=cost*(i+1)-money
        money-=cost*(i+1)
    elif loan !=0:
        loan+=cost*(i+1)
print(loan)

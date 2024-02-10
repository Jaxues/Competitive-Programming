num=int(input())
coins=list(map(int,input().split()))
sum_coins=sum(coins)
coins.sort(reverse=True)
your_sum=0
twin_sum=0
coin_taken=0
taken_now=0
x=1
while x==1: 
    taken_now=coins.pop(0)
    sum_coins-=taken_now
    your_sum+=taken_now
    coin_taken+=1
    if your_sum > sum_coins:
        x=0
print(coin_taken)

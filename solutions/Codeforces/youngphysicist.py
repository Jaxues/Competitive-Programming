num=int(input())
force1=0
force2=0
force3=0
for i in range(num):
    forces=list(map(int,input().split()))
    force1+=forces[0]
    force2+=forces[1]
    force3+=forces[2]

if force1==0 and force2==0 and force3==0:
    print("YES")
else:
    print("NO")


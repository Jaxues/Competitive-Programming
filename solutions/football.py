lineup=input()
counter=0
unlucky_list=[]
for player in range(len(lineup)):
    if player+1 < len(lineup):
        print(lineup[player],lineup[player+1])
        if lineup[player]==lineup[player+1]:
            counter+=1
            print(counter)
        else:
            unlucky_list.append(counter)
            conter=0
print(unlucky_list)
if max(unlucky_list)>=7:
    print("YES")
else:
    print("NO")


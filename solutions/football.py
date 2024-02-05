lineup=input()
counter=0
for player in range(len(lineup)):
    if player+1 < len(lineup):
        print(lineup[player],lineup[player+1])
        if lineup[player]==lineup[player+1]:
            counter+=1
            print(counter)
        
if counter>=7:
    print("YES")
else:
    print("NO")


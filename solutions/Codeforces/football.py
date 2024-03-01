lineup=input()
unluck_counter=0
unluck_max=0
previous=0
for player in range(len(lineup)):
    if player+1 < len(lineup) :

        if lineup[player]==lineup[player+1]:
            unluck_counter+=1
        elif lineup[player]==lineup[player-1] and player!=0:
            unluck_counter+=1 
        else:
            unluck_counter=0
        if unluck_counter>unluck_max:
            unluck_max=unluck_counter
        print(f"first player is {lineup[player]} second player is {lineup[player+1]} They are {lineup[player]==lineup[player+1]}, unluck_counter is {unluck_counter}, unluck_max is {unluck_max}")
        print(f"Previous was {lineup[player-1]}. They are {lineup[player-1]==lineup[player]}")
print(unluck_max)
if unluck_max >= 7:
    print("YES")
else:
    print("NO")

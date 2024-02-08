num_stops=int(input())
passengers=0
list_passengers=[]

for stop in range(num_stops):
    change=list(map(int,input().split()))
    # Remove passengers leaving the tram
    passengers-=change[0]
    # Add passengers boarding tram
    passengers+=change[1]
    list_passengers.append(passengers)

print(max(list_passengers))

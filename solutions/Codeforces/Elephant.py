location=int(input())
steps=0
while location>0:
    if location-5>-1:
        location-=5
        steps+=1
    elif location-4>-1:
        location-=4
        steps+=1
    elif location-3>-1:
        location-=3
        steps+=1
    elif location-2>-1:
        location-=2
        steps+=1
    else:
        location-=1
        steps+=1
print(steps) 

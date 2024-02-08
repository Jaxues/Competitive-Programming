num_participants=input()
response=set(map(int,input().split()))
if len(response)==2:
    print("HARD")
elif 1 in response:
    print("HARD")
else:
    print("EASY")

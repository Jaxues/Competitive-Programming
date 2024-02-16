num_stones=int(input())
intial_arrangement=list(map(str,input()))
num_steps=0
for element in range(len(intial_arrangement)):
    if element+1 < len(intial_arrangement):
        if intial_arrangement[element]==intial_arrangement[element+1]:
            num_steps+=1
print(num_steps)

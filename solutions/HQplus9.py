word_input=input()
instructions=["H","Q","9"]
valid=0
for charater in word_input:
    if charater in instructions:
        valid+=1
if valid > 0:
    print("YES")
else:
    print("NO")

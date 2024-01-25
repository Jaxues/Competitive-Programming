stones=int(input())
sequence=list(map(str,input()))
removed=0
i=0
print(sequence)

for letter in range(len(sequence)):
    if sequence[letter-1]==sequence[letter]:
        removed+=1
        sequence.pop(letter)
print(removed)

intial_word=input()
letters=[]
counter=0
for letter in intial_word:
    counter+=1
    if counter==1:
        letters.append(letter.upper())
    else:
        letters.append(letter)
print("".join(letters))

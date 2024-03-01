word=input()
upper_score=0
lower_score=0
for letter in word:
    if letter == letter.upper():
        upper_score+=1
    elif letter ==letter.lower():
        lower_score+=1

if upper_score > lower_score:
    print(word.upper())
elif lower_score > upper_score:
    print(word.lower())
else:
    print(word.lower())

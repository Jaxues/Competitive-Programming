answered=0
questions=int(input())
for i in range(0,questions):
    answers=input().split()
    if int(answers[0])+int(answers[1])+int(answers[2])>1:
        answered+=1
print(answered)
trails=int(input())
for i in range(0,trails):
    word=input("")
    toolong=len(word)-2
    if toolong>8:
        print("{}{}{}".format(word[0],toolong,word[-1]))
    else:
        print(word)
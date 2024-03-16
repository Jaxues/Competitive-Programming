target=int(input())
final=[]
number=0
while number!=target:
    number+=1
    if number%2==0:
        if number==target:
            final.append("I love it")
        else:
            final.append("I love")
    else:
        if number==target:
            final.append("I hate it")
        else:
            final.append("I hate")


print(" that ".join(final))

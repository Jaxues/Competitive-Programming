year_orgin=int(input())
x=1
while x==1:
    year_orgin+=1
    year_set=set()
    for i in str(year_orgin):
        year_set.add(i)
    if len(year_set)==4:
        break
print(year_orgin) 

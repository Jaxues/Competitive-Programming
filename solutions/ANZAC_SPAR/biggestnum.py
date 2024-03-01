intial_constraints=list(map(str,input().split()))
list_num=[]
counter=0
insert_num=int(intial_constraints[0])
for i in intial_constraints[1]:
    list_num.append(i)

for i in list_num:
    if insert_num > int(i):
        list_num.insert(list_num.index(i),str(insert_num))
        break
    else:
        counter+=1
if counter==len(list_num):
    list_num.append(str(insert_num))

print("".join(list_num))

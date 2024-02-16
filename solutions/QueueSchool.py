intial_num=input()
intial_queue=list(map(str,input()))
final_queue=[]

for person in range(len(intial_queue)):
    print(intial_queue)
    if person+1 < len(intial_queue):
        if intial_queue[person]=="B" and intial_queue[person+1]=="G":
            rearrange=intial_queue.pop(person)
            intial_queue.insert(person,rearrange)
            final_queue.append("G")
        else:
            final_queue.append(intial_queue[person])

print(final_queue)


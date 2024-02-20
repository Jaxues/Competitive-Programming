length=int(input())
intial_array=input().split()
reversed_list=list()

for integer in intial_array:
    reversed_list.insert(0,integer)

print("".join(reversed_list))

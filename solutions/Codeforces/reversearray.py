length=int(input())
intial_array=input().split()
reversed_list=list()
for integer in range(length):
    last=intial_array.pop(-1)
    reversed_list.append(last)
print(" ".join(reversed_list))

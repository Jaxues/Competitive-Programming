number = input()
luck_num={'4','7'}
total_num=0
totaldigitset=set()
for digit in number:
    if digit in luck_num:
        total_num+=1

for total_digit in str(total_num):
    totaldigitset.add(total_digit)

if totaldigitset.issubset(luck_num):
    print("YES")
else:
    print("NO")

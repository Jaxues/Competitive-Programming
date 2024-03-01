sums=input()
factors=[]
for element in sums:
    if element != "+":
        factors.append(element)

print('+'.join(sorted(factors)))

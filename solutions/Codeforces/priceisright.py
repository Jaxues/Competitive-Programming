number=int(input())
items=list(map(int,input().split()))
minimum=items[0]
for item in items:
    if item<minimum:
        minimum=item
print(items.index(minimum))

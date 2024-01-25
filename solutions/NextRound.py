participants, minimum = input().split()
scores = input().split()
nth_place=int(scores[int(minimum)-1])
passed = 0
for i in scores:
    if int(i) >= nth_place and int(i) > 0:
        passed += 1
print(passed)

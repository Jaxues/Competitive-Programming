Berland=input()
Birland=input()
translation=""
for i in range(len(Berland)):
    translation+=Berland[-(i+1)]
if translation.strip()== Birland:
    print("YES")
else:
    print("NO")

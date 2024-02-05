row1=input().split()
row2=input().split()
row3=input().split()
row4=input().split()
row5=input().split()

matrix=[row1,row2,row3,row4,row5]
rownum=0
moves=0
for row in matrix:
    rownum+=1
    if len(set(row))==2:
        moves+=abs(3-rownum)
        moves+=abs(2-row.index("1"))
print(moves)

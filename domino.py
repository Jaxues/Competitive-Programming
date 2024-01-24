height, width=input().split()
height_int=int(height)
width_int=int(width)
dimension=height_int*width_int
X=1
while X==1:
    if dimension%2==0:
        X=0
        print(dimension//2)
    else:
        dimension-=1

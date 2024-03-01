rectangle_area=int(input())
areas=[]
minimum_perimeter=2*(rectangle_area+1)
area_root=int(rectangle_area**0.5)
for i in range(1,area_root+1):
    if rectangle_area%i==0:
        areas.append([i,rectangle_area//i])
for area in areas:
    if 2*(sum(area)) < minimum_perimeter:
        minimum_perimeter=2*(sum(area))
print(minimum_perimeter)


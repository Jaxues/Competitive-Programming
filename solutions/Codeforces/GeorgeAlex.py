num_rooms = int(input())
avaliable = []
num_avaliable_rooms = 0
for room in range(num_rooms):
    avaliable.append(list(map(int, input().split())))


for avaliable_room in avaliable:
    if (
        avaliable_room[0] != avaliable_room[1]
        and avaliable_room[0] + 2 < avaliable_room[1]
    ):
        num_avaliable_rooms += 1
print(num_avaliable_rooms)

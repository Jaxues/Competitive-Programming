num_magnets = int(input())
mag_sequence = list()
total = 1
for i in range(num_magnets):
    mag_value = input()
    mag_sequence.append(mag_value)

for magnet in range(len(mag_sequence)):
    if magnet < len(mag_sequence) - 1:
        if mag_sequence[magnet] != mag_sequence[magnet + 1]:
            total += 1
print(total)

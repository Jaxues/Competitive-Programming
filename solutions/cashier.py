intial_constraints = list(map(int, input().split()))
time_work = intial_constraints[1]
break_time = intial_constraints[2]
customer_num = intial_constraints[0]
breaks = 0
for i in range(customer_num):
    custom_constraints = list(map(int, input().split()))
    print(
        f"Customer arrives {custom_constraints[0]} after starting takes {custom_constraints[1]} to serve them."
    )


while time_work >= 0:

    print(f"Still has {time_work} left. Break is {break_time} long")
    if time_work - break_time >= 0:
        breaks += 1
        time_work -= break_time
    elif time_work - break_time < 0:
        break
print(breaks)

messages = int(input())

for message in range(messages):
    num, charge, consumptionmessage, consumptionidle = input().split()
    battery = int(charge)
    consumptionmessageint = int(consumptionmessage)
    consumptionidleint = int(consumptionidle)
    for i in range(int(num)):
        cases = input().split()
        z = 0
        for x in cases:
            z += 1
            if z % 2 == 0:
                consumed_message = int(consumptionmessageint * x)
                battery = -consumed_message
            else:
                consumed_idle = int(consumptionidleint * x)
                battery = -consumed_idle
        if battery > 0:
            print("YES")
        else:
            print("NO")

import time

for i in range(2):
    if i == 0:
        for var in range(1,13):
            print((str)(var)+'AM')
            time.sleep(0.25)
    elif i == 1:
        for var in range(1,13):
            print((str)(var)+'PM')
            time.sleep(0.25)
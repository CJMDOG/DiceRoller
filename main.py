import random

# low = None
# high = None
while True:
    try:
            low = 1
            high = int(input('Which Dice?'))
            roll = random.randint(low, high)
            if roll == low:
                print("Crit Fail! Your Mom Fucked up! " + str(roll))
            elif roll == high:
                print("Crit Success! You walked into the right house motha trucka! " + str(roll))
            else: print(roll)                             
    except ValueError:
            print("Don't be stupid, we need a number!")

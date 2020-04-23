import random
 
while True:
    print("This is an infinite loop")
    rand_num = random.randint(1, 101) # random integer between 1 and 100
    if rand_num > 75:
        print("The loop has ended")
        break # stop the loop

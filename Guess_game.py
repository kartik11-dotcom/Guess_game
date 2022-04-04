import random

flag = True
attempt = 0
print("****\tGuess Game\t****")
num = random.randint(1,100)
print("Select Difficulty level:")
ch = input("Easy(e), Medium(m) Hard(h): ")


if ch == 'e':
    att_remain = 8
elif ch == 'm':
    att_remain = 6
elif ch == 'h':
    att_remain = 4

print(f"You have {att_remain} attempts.")

while(flag):
    enter = int(input("Guess a number between 1 to 100: "))
    attempt += 1
    if(enter > num):
        print("Try smaller number")
        att_remain -= 1
    elif(enter < num):
        print("Try larger number")
        att_remain -= 1
    elif(enter == num):
        print("Guessed correct Number!!")
        print("You Won!!")
        flag = False
        break

    if(num > enter):
        remain = num - enter
        if(remain <= 10):
            print("Too close!! (1-10)")
        elif(remain > 10 and remain <=25):
            print("A bit far! (11-25)")
        elif(remain > 25 and remain <= 50):
            print("Far!! (26-50)")
        elif(remain > 50):
            print("Too far!! (51-100)")
    
    if(num < enter):
        remain = enter - num
        if(remain <= 10):
            print("Too close!! (1-10)")
        elif(remain > 10 and remain <=25):
            print("A bit far! (11-25)")
        elif(remain > 25 and remain <= 50):
            print("Far!! (26-50)")
        elif(remain > 50):
            print("Too far!! (51-100)")
    
    print("Attempt remaining: ",att_remain)
    if(att_remain == 0):
        flag = False
        print("You Lost!!")

print("Attempt took: ",attempt)
print("Game Over!!")
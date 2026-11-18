import random as rd

correct_number = rd.randint(1,100)
attempts = 0

print("猜数字即将开始")



while True:
    guess = int(input("请输入你猜的数字："))
    attempts += 1
    if guess < correct_number:
        print("猜小了")
    elif guess > correct_number:
        print ("猜大了")
    else:
        print(f"终于猜对了，你一共猜了{attempts}次")   
        break
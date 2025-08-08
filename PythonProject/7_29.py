# print("hello world")
# for a in range (1 ,10):
#     message = "这是第%d个数字"% a
#     print(message)
# nums = input("Input a number: ")
# nums = int(nums)
# for a in range(nums):
#     # if a>=5:
#     #     break
#     print(a)
#
# nums = 0
# for i in range(101):
#     nums+=i
# print(nums)



#Guess Number
# from random import randrange
#
# print("Let's play a game!!!")
# while True:
#     numberRange = input("Input the number range you want to guess: ")
#     numberRange = int(numberRange)
#     num = randrange(1,numberRange+1)
#     try_sum = 1
#     while True:
#         guess = input("Guess the number: ")
#         guess = int(guess)
#         if guess>num:
#             print("Larger")
#             try_sum+=1
#         elif guess<num:
#             print("Smaller")
#             try_sum+=1
#         else:
#             print(f"Nice work! You use {try_sum} times to reach the target number")
#             break
#
#     again = input("Would you like to try again(y/n)?")
#     if again == 'n':
#         print("Game Over!")
#         break
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}" ,end =' ')
#     print("\n")


from Play_game import play_game

# def play_game():
#     numberRange = input("Input the number range you want to guess: ")
#     numberRange = int(numberRange)
#     num = randrange(1, numberRange + 1)
#     try_sum = 1
#     while True:
#         guess = input("Guess the number: ")
#         guess = int(guess)
#         if guess > num:
#             print("Larger")
#             try_sum += 1
#         elif guess < num:
#             print("Smaller")
#             try_sum += 1
#         else:
#             print(f"Nice work! You use {try_sum} times to reach the target number")
#             return
#

print("Let's play a game!!!")
while True:
    play_game()
    again = input("Would you like to try again(y/n)?")
    if again == 'n':
        print("Game Over!")
        break



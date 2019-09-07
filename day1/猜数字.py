#1、随机产生一个1-100之间的数字
#2、输入一个1-100之间的数字，
#3、总共7次机会
#4、如果猜大了，提示猜大了，继续猜，
#5、如果猜对了，就结束游戏

# while循环写的
# import random
# number = random.randint(1,100) #随机产生一个1-100之间数字
# print(number)
# count = 0
# while count<7:
#     count = count + 1
#     guess = input('请输入一个数字：')
#     guess = int(guess)
#     if guess == number:
#         print('恭喜你猜对了，游戏结束')
#         break
#     elif guess<number:
#         print('猜小了')
#         continue
#     else:
#         print('猜大了')
#         continue
# else: #while对应的else的作用是，循环正常结束之后，会执行else里面的代码
#     print('错误次数已经用完')



import random
number = random.randint(1,100) #随机产生一个1-100之间数字
print(number)
for i in range(7):
    guess = input('请输入一个数字：')
    guess = int(guess)
    if guess == number:
        print('恭喜你猜对了，游戏结束')
        break
    elif guess<number:
        print('猜小了')
        continue
    else:
        print('猜大了')
        continue

else: #while对应的else的作用是，循环正常结束之后，会执行else里面的代码
    print('错误次数已经用完')


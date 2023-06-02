# while loops

# from re import X

x=0
while (x<=5):
    print(x)               # #loop means print when x 5 tak pounch jahay
    x=x+1           #increment is also necessary

from math import factorial


1 # for loop

# for x in range(6,12):
#     print(x)

2 # array

days =["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
     if (d=="fri"):break
     print(d)

# 3 array

days =["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
    if (d=="fri"):continue
    print(d)

# simple situation

# count = 0
# while count<9:
#     print("Number:",count)
#     count =count+1

# print("good bye")

# little guessing game

# import random
# n = 20
# to_be_guessed = int(n * random.random())+1
# guess = 0

# while guess != to_be_guessed:
#     guess = int(input("New number:"))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print("Number is to large")
#         elif guess < to_be_guessed:
#                 print("Number is to small")
#     else:
#         print("you are giving it!")
#         break
# else:
#         print("congratulations you made it!")

# For loop 
# 1 in for loop you know how many times statment is printed
# 2 for loop provides a syntax in which following information
# is provided
# - Boolean condition
# - intial value of counting variable
# - incrementation of counting variable

# fruits = ['mangoes','apples','bananas']

# for fruit in fruits:
#     print("current fruit:",fruit)

# print("good bye")


# 1.3  let find Factorial 
# - we know the iteration so for is the better options

# num =int(input("Number:"))
# factorial=1

# if num < 0:
#     print("must be positive")
# elif num == 0:
#     print("factorial=1")
# else:
#     for i in range(1,num + 1):
#         factorial=factorial*i
# print(factorial)




# 1.4  Nested loop
# example of nested while loop
# in this python program use a loop inside another loop.
# in printing bank machine(atm)

# print('Wellcome to Anas Awan bank')
# restart =('Y')
# chances= 3
# balance = 67
# while chances >=0:
#     pin=int(input('please enter your 4 digit pin:\n'))
#     if pin ==(1234):
#         print('You entered your pin correctly\n')
#         while restart not in ('n','NO','no','N'):
#             print('Please Press 1 For Your Balance\n')
#             print('please press 2 to make a withdrawal\n')
#             print('please press 3 to pay in\n')
#             print('please press 4 to return card\n')
#             option = int(input('what would you like to chose?'))
#             if option== 1:
#                 print('your balance == $',balance,'\n')
#                 restart=input('would you like to go back?')
#                 if restart in('n','NO','no','N'):
#                     print('thankyou')
#                     break
#             elif option==2:
#                 option2 =('y')
#                 withdrawal = int(input('how much you want to withdrawal? 10/20/40/50/70 for other amount:\n'))
#                 if withdrawal in [10,20,40,50,70]:
#                     balance = balance - withdrawal
#                     print=(' your balance is now ',balance,'\n')
#                     restart=input('would you like to go back')
#                     if restart in ('n','No','no','N'):
#                         print('thankyou')
#                         break
#             elif withdrawal !=[10,20,40,50]:
#                 print('invalid amount,please Re_try\n')
#                 restart= ('y')
#             elif withdrawal == 1:
#                 withdrawal =int(input('please input Desired amount'))

#             elif option== 3:
#                 Pay_in=int(input('how much you like to pay in?'))
#                 balance=balance+Pay_in
#                 print('\n your bank balance is now$',balance)
#                 restart('would you like to go back?')
#                 if restart in ('n','No','no','N'):
#                     print('thankyou')
#                     break
#             elif option== 4:
#                 print('please wait whilist your card is returned...\n')
#                 print('thankyou for your service')
#                 break
#             else:
#                 print('please enter a correct number\n')
#                 restart=('y')
#     elif pin != (1234):
#         print('incorrect answer')
#         chances=chances-1
#         if chances==0:
#          print('no more tries')
#         break


# 1.5 nested loop for example



        






# # print('HelloWorld')
# # # firstName = "Rohit"
# # # lastName = "Joshi"
# # # print(firstName + ' ' + lastName)
# #
# # print("This line\nspilt\t2\t3")
# #
# # print('24' + ' 36')
# #
# # a = 12
# # b =7
# # print(a//b)
# #
# # a=5
# # print("Hello {0} {1}".format(a,4))
#
# import random
# a=0
# inputText="Y"
# while inputText == "Y":
#     randomNumber =random.randint(1,6)
#     while a==0:
#         inputNumber = input("Guess the Number ")
#         if int(randomNumber)==int(inputNumber):
#             print("You Won")
#             a=1
#         elif int(randomNumber) < int(inputNumber):
#             print("Choose a smaller Number")
#         elif int(randomNumber) > int(inputNumber):
#             print("Choose a larger Number")
#     a=0
#     inputText = input("Do you want to continue playing? Y/N ")

# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
#
# if 18 < age < 31:
#     print("Welcome {0}, you have been checked in".format(name))
# elif age < 18:
#     print("I apologize {0}, please come back in {1} years".format(name,18-age))
# else:
#     print("I apologize {0}, you are no longer eligible for the holiday".format(name))

# st='eat,play'
# test='test'
# final=''
# count=1
# for i in "rt-rr","df-cv":
#     print("enter for")
#     if i in ("abcdefghijkltestmopqrstuvwxyz"):
#         final = final+i
#         print(final)


# ipAddress = input("Please enter an IP address ")
# count = 1
# segment = ''
# for i in range(0, len(ipAddress)):
#     if ipAddress[i] == ".":
#         count += 1
#         if len(segment) != 0:
#             print("Segment {0} is {1} and is {2} characters long".format(count-1, segment, len(segment)))
#
#         segment = ''
#     else:
#         segment += ipAddress[i]
# else:
#     count += 1
#     if len(segment) != 0:
#         print("Segment {0} is {1} and is {2} characters long".format(count-1, segment, len(segment)))
#         count -= 1
#
#
# print("There is/are {0} segment(s)".format(count-1))

str = ["a","b"]
print (str[1])
# Write a program that allows the user to enter five numbers (read as strings).
# Create a string that consists of the user’s numbers separated by plus signs.
# For instance, if the user enters 2, 5, 11, 33, and 55, then the string should be ‘2+5+11+33+55’.

# text = input("enter numbes: ")
# text = text.split(" ")
# text="+".join(text)
# print(text)
#--------------------------------------------
# Write a program that gets a string from the user containing a
# potential telephone number. The program should print Valid
# if it decides the phone number is a real phone number, and
# Invalid otherwise. A phone number is considered valid as
# long as it is written in the form abc-def-hijk or 1-abc-def-hijk.
# The dashes must be included, the phone number should contain
# only numbers and dashes, and the number of digits in each group
# must be correct. Test your program with the output shown below.

# number= input("Phone number: ")
#
# if number[3]=="-" and number[7]=="-" and number[0:2].isdigit() and number[4:6].isdigit() and number[8:11].isdigit() or \
# number[1] == "-" and number[5] == "-" and number[9] == "-" and number[0].isdigit() and number[2:4].isdigit() and \
# number[6:8].isdigit() and number[10:13].isdigit():
#     print("Valid")
# else:
#     print("Invalid")

#--------------------------------------------------------------------



# Write a program that implements the Caesar cipher, a simple
# encryption technique where each letter in the plaintext is
# shifted a certain number of places down the alphabet

# text = input("enter text")
# step = int(input("enter step"))
# step = (step % len(text))
#
# newtext=""
#
# for i in range(len(text)-step,len(text)):
#     newtext += text[i]
# for i in range(len(text)-step):
#     newtext += text[i]
#
# print(newtext)

#--------------------------------------------------------------
#
# Write a program that calculates the Fibonacci sequence.
# The Fibonacci sequence is a series of numbers where each
# number is the sum of the two numbers preceding it. The
# first two numbers are 0 and 1, and the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
#
# n = int(input("Enter num Fibonacci: "))
#
# a=0
# b=1
# c=1
# if n==1:
#     print(0)
# else:
#     print(0,1,1,end=" ")
#     for i in range(n-3):
#         a=b
#         b=c
#         c=b+a
#         print(c,end=" ")

#---------------------------------------------------------


# Write a program that accepts a string from the user and removes
# all duplicates. The resulting string should contain only unique characters.

# text = "hello world"
# mylist = []
# for i in text:
#     mylist.append(i)
#
# for  i in mylist:
#     while mylist.count(i)!=1:
#         mylist.remove(i)
#
# text="".join(mylist)
#
# print(text)
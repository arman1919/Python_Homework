# Write a program that generates and prints 50 random integers, each between 3 and 6.
# import random
#
# for i in range(51):
#     print(random.randint(3,6),end=" ")

# Write a program that asks the user to enter two numbers, x and y , and computes | x − y | /  x + y

# x= int(input("X-"))
#
# y= int(input("Y-"))
# if x > y:
#     num= ((x-y))/(x+y)
# else:
#     num = ((y-x)) / (x + y)
# print(num)

# Write a program that checks if a string is a palindrome.

# text=input("enter text")
# j=len(text)-1
# x="polindrome"
# for i in text:
#     if i != text[j]:
#         x="no palindrome"
#     j-=1
#
# print(x)
# Write a program that takes a list of numbers and calculates the sum of its elements.

# mylist=[1,2,3,4,5]
# sum=0
#
# for i in mylist:
#     sum += i
#
# print("sum list=",sum)

# Write a program that takes a list of numbers and returns the largest number in the list.

# mylist=[1,2,3,4,5]
# max=mylist[0]
# for i in mylist:
#     if max<i:
#         max=i
#
# print("max=",max)

# Write a program that reverses a string.

# text="hello"
# newtext=""
#
# for i in reversed(text):
#     newtext +=i
#
# text = newtext
#
# print(text)

# Write a program that calculates the area of a circle given its radius.

# radius = int(input("radius-"))
# area = 3.14 * radius **2
# print(area)
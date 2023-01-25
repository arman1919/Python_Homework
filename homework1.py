# Write a program that asks the user to enter a number, 
# checks, and prints whether the number is even or odd.

# x=int(input("Enter num"))
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")

#---------------------------------------------------
# Write a program that asks the user to enter a character,
# checks, and prints whether the character is a consonant or a vowel.

# consonant="AEIOUYaeiouy"
# x=input("Symbol-")
# if x in consonant:
#     print("Symbol is consonant")
# else:
#     print("Symbol is vowel")

#---------------------------------------------------

# Write a program that asks the user to enter 
# n number and prints the nth Fibonacci number.

# n=int(input("Enter num"))
# c=2
# if n==1 or n==2:
#     c=1
# x=1
# y=1
# for i in range(n-3):   
#     c=y+c
#     y=y+x
#     x=c-y

# print(c)

#---------------------------------------------------

# Write a program that asks the user to enter a 
# number and prints the sum of its digits on the screen. 

# n=int(input("Enter num"))
# summ=0
# while n !=0:
#     summ += n%10
#     n//=10

# print(summ)

#---------------------------------------------------
# program that prints the following
# image on the screen. Use cycles.

    #    * * * * *
    #   *         *
    #   *         *
    #   *         *
    #    * * * * *
# print(" ",end="")
# for i in range(6):
#     print("*",end=' ')
# print(" ")
# for i in range(4):
#     print("*",end="")
#     for j in range(11):
#         print(" ",end="") 
#     print("*")
# print(" ",end="")
# for i in range(6):
#     print("*",end=' ')

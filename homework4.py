# Իրականացնել ծրագիր, որում պետք է ստեղծել ցուցակ(list),
# բաղկացած 100-ից 1000-ի միջև ընկած բոլոր պալինդրոմային
# թվերից՝ օգատգործելով list-ի comprehension։

# def polidrom(x):
#
#     n=str(x)
#     j=len(n)-1
#     for i in range(len(n)):
#         if n[i] != n[j]:
#             return False
#         j -= 1
#     return True
#
#
# polilist = [i for i in range(100,1001) if polidrom(i)]
#
# print(polilist)
#-----------------------------------------------------------
# Իրականացնել ծրագիր, որը շրջում է մատրիցը 180 աստիճանով։
# Input:
# 1   2   3   4
# 5   6   7   8
# 9   10  11  12
# 13  14  15  16
# Output:
# 16  15  14  13
# 12  11  10  9
# 8   7   6   5
# 4   3   2   1

# matric =[]
# linelist=[]
# line = int(input("Line-"))
# real = int(input("Real-"))
#
#
# for i in range(line):
#     for j in range(real):
#         x = int(input())
#         linelist.append(x)
#     matric.append(linelist)
#     linelist=[]
#
#
# for i in range(line-1,-1,-1):
#     for j in range(real-1,-1,-1):
#         print(matric[i][j],end=" ")
#     print()

#---------------------------------------------------------

# Ունենք ամբողջ թվերից բաղկացած մատրից, որի վրա
# պետք է իրականացնել transpose։ Transpose կատարել
# նշանակում է մատրիցի տողերը փոխադրել սյուներով։
# Input:
# matrix = [[1, 2, 3] ,[4, 5, 6] ,[7, 8, 9]]
# Output:
# transposed = [[1, 4, 7] ,[2, 5, 8] ,[3, 6, 9]]

# matrix = [[1, 2, 3] ,[4, 5, 6] ,[7, 8, 9]]
# linelist =[]
#
# newmatrix=[]
#
# for i in range(3):
#     for j in range(3):
#         linelist.append(matrix[j][i])
#     newmatrix.append(linelist)
#     linelist =[]
#
# for i in range(3):
#     for j in range(3):
#         print(newmatrix[i][j],end=" ")
#     print()
#---------------------------------------------------------

# Գրել ծրագիր, որը կստուգի մուտքային թիվը երկուսի աստիճան է, թե՝ ոչ։

# def extent(n):
#     x=1
#
#     while x<=n:
#         if x==n:
#             return True
#         x *= 2
#     return False
#
# N = int(input("Num-"))
#
# print(extent(N))
#---------------------------------------------------------

# Գրել ծրագիր, որը որպես մուտքային արժեք
# կստանա ամբողջ թիվ և կարտածի նրանում պարունակվող ‘1’ բիթերի քանակը։
#
# def bullian(n):
#     b=''
#     while n !=0:
#         b += str(n%2)
#         n //= 2
#     return b[::-1]
#
# x= int(input("num-"))
# caunt=0
#
# for i in bullian(x):
#    if i=='1':
#        caunt += 1
#
# print(caunt)
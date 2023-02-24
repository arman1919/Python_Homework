# Տրված է list, որը պարունակում է 1-ից n ամբողջ թվերը(1-ը ներառյալ)։
# Գրել ֆունկցիա, որը որպես պարամետր կստանա այդ list-ը և կգտնի բացակայող
# թիվը։ Բացակայող թիվ չգտնելու դեպքում վերադարձնել None։

# def lostnum(ls):
#     if ls[0] != 1:
#         return 1
#     for i in range(1,len(ls)):
#         if ls[i] != ls[i-1]+1:
#             return ls[i]-1
#
#     return None
#
#
# number = [1,2,3,4,5,6,7,9]
#
# print(lostnum(number))

# Իրականացնել ֆունկցիա (add_exictment), որը որպես պարամետր
# կստանա string-երից բաղկացած list և կավելացնի բացականչական
# նշան (!) յուրաքանչյուր string-ի վերջում։ Ծրագիրը պետք է
# փոփոխի սկզբնական list-ը և ոչինչ չվերադարձնի։

# def add_exictment(str_lsit):
#
#     for i in range(len(str_lsit)):
#         str_lsit[i] += '!'
#
#
#
# str_list = ['text1','text2']
# add_exictment(str_list)
# print(str_list)

# Գրել sum_digits անունով ֆունկցիա, որը վերադարձնում
# է իրեն փոխանցված ամբողջ թվի թվանշանների գումարը:
# Գրել is_sorted անունով ֆունկցիա, որը որպես պարամետր
# կստանա list և կվերադարձնի True, եթե ցուցակը սորտավորված
# է և False, հակառակ դեպքում
#
# def sum_digits(num):
#     summ = 0
#     while num != 0:
#         summ += num %10
#         num //= 10
#     return summ
#
# def is_sorted(ls):
#     newls = ls.copy()
#     ls.sort()
#     if ls == newls:
#         return True
#     else:
#         return False
#
#
# print(sum_digits(12345))
#
# list0 = [1,2,3,5,7,8,9,10,1,5,6]
#
# print(is_sorted(list0))

# Իրականացնել ֆունկցիա, որը որպես պարամետր կստանա երկու
# list կմվիավորի դրանք։ List-երը արդեն իսկ սորտավորված են։

# def joinlist(ls1,ls2):
#     ls1.extend(ls2)
#
#
# ls1 = [1,2,3,4,5]
# ls2 = [6,7,8,9,10]
#
# joinlist(ls1,ls2)
#
# print(ls1)

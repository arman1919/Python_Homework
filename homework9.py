# Իրականացնել ռեկուրսիվ ֆունկցիա, որը կհաշվարկի փոխանցված ամբողջ
# թվի ֆակտորիալը։ Նաև պետք է ստուգել՝ արդյոք փոխանցված
# արգումենտը հանդիսանում է ամբողջ թիվ, թե ոչ։

# def faktor(a):
#     if not str(a).isdigit():
#         return "number is not integer"
#     if a < 1: return 1
#
#     return  a * faktor(a-1)
#
#
# x = 5
# print(faktor(x))
# x = "hello"
# print(faktor(x))


# enumerate ներկառուցված մեթոդը ավելացնում է հաշվիչ (counter)
# իտերացվող օբյեկտի վրա և վերադարձնում է enumerate օբյեկտ, որն
# է իր հերթին հնարավոր է ներկայացնել list-ի տեսքով։ Իրականացնել
# պարզագույն enumerate ֆունկցիա, որն առաջին արգումենտով կստանա
# իտերացվող օբյեկտը (պետք է ստուգում կատարել՝ արդյոք փոխանցված
# օբյեկտը իտերացվող է), իսկ երկրորդ արգումենտով start, որն էլ
# նշանակում է հաշվարկի սկիզբը(default 0 է վերագրված)։
# Վերադարձվող օբյեկտը կարող է լինել tuple-ների list։

# def enumerate(ls,start = 0):
#     try:
#         iter(ls)
#     except TypeError:
#         return "no iterable"
#     for i in range(start,len(ls)):
#         yield i,ls[i]
#
#
#
# ls = [1,2,3,4,5,6]
# a = 5
# for i in enumerate(ls,1):
#     print(i)

# filter ներդրված ֆունկցիան ստանում է երկու արգումենտ
# և վերադարձնում իտերատոր։ Եթե ֆունկցիան None է, ապա
# վերադարձվում են միայն այն էլեմենտները, որոնք true
# են։ Իրականացնել filter ֆունկցիան։

# def my_filter(func,iterable):
#     for element in iterable:
#         if func in None:
#             if element:
#                 yield element
#         elif func(element):
#             yield element


# Իրականացնել ֆունկցիա, որը որպես արգումենտ կստանա
# ամբողջ թիվ և կվերադարձնի True, եթե այդ թիվը չորսի
# աստիճան է և False` հակառակ դեպքում։
# Խնդիրը իրականացնել հնարավորինս օպտիմալ եղանակով


# def astichan4 (x):
#     if x == 4 or x == 1:
#         return True
#
#     a= "{0:b}".format(x)
#     if (len(a) - 2) % 3 !=0:
#         return False
#
#     if a[0] == '1' and a[1:] ==( len(a)-1) * "0":
#         return True
#
#     return False
#
# x = 1
#
# print(astichan4(x))
#
# x = 4
#
# print(astichan4(x))
#
# x = 1024
#
# print(astichan4(x))
#
# x = 13
#
# print(astichan4(x))


# 4 ի n աստիճանի բոլոր թվերի երկուական ներյաըացումը
# ունեն 10 000 000 ․․․ տեսքը բացառությամբ 1 ի և 4 ի
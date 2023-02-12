# Իրականացնել պարզագույն բառարան, որը ֆայլից կկարդա բառերի համախումբ՝
# անգերեն-հայերի բառերի թարգմանությամբ։ Բառերը կարող են լինել Python
# keyword-ներ, statement-ներ և այլ համակարգչային գիտությանը վերաբերվող
# բառեր։ Օբյեկտը, որի մեջ պետք է պահեք բառերը, կարող է լինել dictionary։


# import Dictionary
#
# def Translite(n):
#     if n in Dictionary.words.keys():
#         print(Dictionary.words[n])
#     else:
#         print("there is no such word in the dictionary")
#
#
# word = input("Enter Translite word :")
#
# Translite(word)



# Տրված է հետևյալ ֆունկցիան def myfunc(alist): . . . . return len(alist)։
# dis module-ի օգնությամբ դուրս բերել բայթ կոդի ներկայացումը և նկարագրել
# բոլոր դաշտերը (Python byte-code)։


# import dis
#
# def myfunc(alist):
#     return len(alist)
#
#
# print(dis.dis(myfunc))
#

# 30               0 LOAD_GLOBAL 0(len)     "Ստեկում ավելացնում է len ֆունկցիան գլոբալ տիրույթից"
#
# 2 LOAD_FAST                0 (alist)      "Ստեկում ավելացնում է alist արգումենտր"
#
# 4 CALL_FUNCTION            1              "Կանչում է len ֆունկցիան  alist արգումենտով"
#
# 6 RETURN_VALUE                        "վերադարձնում է len փունկցիաի վերադարձրաց արժեքը"

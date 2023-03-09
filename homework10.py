# Իրականացնել map, reduce, range ֆունկցիաները
# օգտագործելով գեներատոր ֆունկցիաներ։

# def my_map(func,iterable):
#     for i in iterable:
#         if func(i):
#             yield i
#
# def zuyg(x):
#     return x % 2 == 0
#
#
# ls = [1,2,3,4,5,6,7,8,9]
#
# print(list(my_map(zuyg,ls)))

# def my_reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value
#
# def gumar(x,y):
#     return x + y
#
# ls = [1,2,3,4,5,6,7,8,9]
#
# print(my_reduce(gumar,ls))

# def my_range(stop,start = 0):
#     if start == 0:
#         x = 0
#         while x != stop:
#             yield x
#             x += 1
#     else:
#         x = stop
#         while x != start:
#             yield x
#             x += 1
#
# print(list(my_range(10,15)))



# Իրականացնել սեփական MyIterable class-ը, որը կունենա iter և next ատրիբուտները։

# class MyIterable:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def my_iter(self):
#         return self
#
#     def my_next(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = self.data[self.index]
#         self.index += 1
#         return value
#
#
# ls = MyIterable([1,2,3,4,5])
#
# a = ls.my_iter()
# b = ls.my_next()

# Իրականացնել for օգտագործելով iterator։

# ls = [1,2,3,4]
#
# iter_ls = iter(ls)
#
# x = 0
# while x != len(ls):
#     i = next(iter_ls)
#     print(i)
#     x += 1


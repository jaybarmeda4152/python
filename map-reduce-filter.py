##  MAP function ###
'''
-map function no second parameter a one by one element lese ene first parameter ma je function hase ama pass karse,
ane a function mathi je value return karse ene ek list ma store kartu jase.
-map function ma eklu list nai pan set, tuple ma pan store kari sakay, dictionary ma store na thay.
'''
# a = [1,2,3,4,5]
# def testfunc(digit):
#     return digit*100
# # b = list(map(lambda x: x*x,a))
# b = tuple(map(testfunc,a))
# print(b)


## FILTER function ###

# a = [1,2,3,4,5]
# def funCube(digit):
#     return digit > 3

# b = list(filter(funCube,a))
# print(b)

## REDUCE function ###
'''
reduce funciton a only 2 j argument le ana thi vadhare na le.
ama avu hoy ke jyare function call thay tyare list na pela 2 element ane anu je result ave ane first argument ma store kare.
pa6i next time first argument ma result hoy ane second argument ma next element hoy list no.
'''
from functools import reduce
# def funCube(key,digit):
#     if key > digit:
#         print('true=> ',key)
#         return key + digit
#     else:
#         print('false=> ',key)
#         return key * 2

a = [1,2,3,4,5,6]
b = reduce(lambda x,y: x+1 if x > y else x*2,a)
# b = reduce(funCube ,a)
print(b)
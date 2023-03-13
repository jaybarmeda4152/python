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

a = [1,2,3,4,5]
def funCube(digit):
    return digit ** 3

# print(a)
b = list(filter(funCube,a))

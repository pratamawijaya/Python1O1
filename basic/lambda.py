# x = lambda a : a + 10
# print(x(5))

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2)

print(myDoubler(11))
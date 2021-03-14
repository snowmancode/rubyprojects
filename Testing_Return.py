def returnFunction(num):
    num = num * 2
    return num


returnFunction(4)

def printFunction(num):
    num = num * 2
    print(num)

printFunction(2)

def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"

f1 = function_that_prints()
f2 = function_that_returns()
print("Now let us see what the values of f1 and f2 are")
print(f1)
print(f2)

function_that_prints()
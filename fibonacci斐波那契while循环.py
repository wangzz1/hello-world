word = int(input("Press n\' value:"))

def foo(x):
    n = 1
    a = 0
    b = 1
    while n < x:
        
        i = b
        b = a+b
        a = i
        n += 1
    return a


print(foo(word))

def fact(x):
    if(x > 1):
        return (x * fact(x-1))
    else:
        return (1)
print(fact(4))

input()
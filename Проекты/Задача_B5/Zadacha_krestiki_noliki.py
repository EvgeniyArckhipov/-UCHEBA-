a = [1, 4, 5, 7, 8]
def kvadrat(x):
    return x**2

c = list(map(kvadrat, a))
print(c)

d = list(map(lambda x: x+2, a))
print(d)
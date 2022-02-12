class Rotata:
    name = "Жопа"
    age = 31
a = Rotata()
print(Rotata.name)
print(a.__dict__)
print(Rotata.__dict__)
Rotata.weight = 73
print(Rotata.__dict__)
a.b = 1000
print(a.b)
setattr(Rotata, "name", "Жопааа")
print(Rotata.__dict__)
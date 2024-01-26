def add(*args):
    #print(sum(args))
    summa = 0
    for n in args:
        summa += n
    return summa

print(add(1,2,3,4,5,6,7))

def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Kia")
print(my_car.model)
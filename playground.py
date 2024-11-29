#def add(*args):
#    sum = 0
#    for n in args:
#        sum += n
#    return sum
#
#print(add(3,4,5))

def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(model="GT")
print(my_car.model)
class Descriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.value]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value of {} should be positive.".format(self.value))
        else:
            instance.__dict__[self.value] = value


class BePositive:
    number = Descriptor(int)


val_one = BePositive()
val_two = BePositive()

val_one.number = 0  # Error
val_one.number = 1
print(val_one.number)
val_two.number = 2
print(val_one.number)
print(val_two.number)
val_two.number = -10  # Error
print(val_one.number)
print(val_two.number)

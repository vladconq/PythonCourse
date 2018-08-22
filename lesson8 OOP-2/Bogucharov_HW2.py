class EnumMeta(type):
    def __new__(cls, name, bases, dict):

        dict['__mapping__'] = {}
        members = {k: v for (k, v) in dict.items() if not (k.startswith('__') and k.endswith('__'))}
        enum = super().__new__(cls, name, bases, dict)
        for key, value in members.items():
            value = enum(value)
            value.name = key
            setattr(enum, key, value)
        return enum

    def __iter__(self):
        return (self.__name__ + "." + name for name in self.__dict__.keys() if
                not (name.startswith('__') and name.endswith('__')))

    def __getitem__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            return "KeyError: '{}'".format(item)


class Enum(metaclass=EnumMeta):
    __mapping__ = {}

    def __new__(cls, value):
        if value in cls.__mapping__:
            return cls.__mapping__[value]
        v = super().__new__(cls)
        v.value = value
        v.name = ''
        cls.__mapping__[value] = v
        return v

    def __repr__(self):
        if self.name in Direction.__dict__:
            return '<{}.{}: {}>'.format(self.__class__.__name__, self.name, self.value)
        else:
            return "ValueError: {} is not a valid Direction".format(self.value)


class Direction(Enum):
    north = 0
    east = 90
    south = 180
    west = 270


print(Direction.north)
print(Direction.south)
print(Direction.north.name)
print(Direction.north.value)
print(Direction(0))
print(Direction(30))
Direction(30)

for d in Direction:
    print(d)

print("id of Direction.north: " + str(id(Direction.north)))
print("id of Direction(0): " + str(id(Direction(0))))

print(Direction['west'])
print(Direction['north-west'])

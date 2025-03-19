class ValidFullNameclass:
    def __init__(self, name):
        self.name = name
        self.value = None

    def __set__(self, instance, value):
        if value[4:].isalpha():
            instance.__dict__[self.number] = value
        else:
            raise ValueError("Value must be only letters" )
        
class MyClass:
    name = ValidFullNameclass("Burxoniddin")
c = MyClass()
c.name = "1Burxoniddin"
print(c.name)


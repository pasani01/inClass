class PositiveBalance:
    def __init__(self, name):
        self.name = name
        self.value = None
        print(f"{self.name} was created")

    def __get__(self, instance, owner):
        print(f"{self.name} was called")
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value")
        instance.__dict__[self.name] = value
        print(f"{self.name} was set")

    def __delete__(self, instance):
        print(f"{self.name} will deleted")
        del instance.__dict__[self.name]


class BankAccount:
    balance = PositiveBalance("balance")

customer = BankAccount()
customer.balance = 1
print(customer.balance)
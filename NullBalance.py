class BalanceDescriptor:
    def __init__(self, name):
        self.name =name
        self.value=None

    def __get__(self, instance, owner):
        if instance.__dict__[self.name] is None:
            return self.name
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value,float) and value>0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Balance must be > 0  and number")


class Balance:
    account=BalanceDescriptor("account")

p=Balance()

p.account=4566546.45
print(p.account)
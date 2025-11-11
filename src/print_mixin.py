class PrintMixin:

    def __init__(self):
        try:
            print(repr(self))
        except ValueError as e:
            return 0

    def __repr__(self):
        try:
            return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
        except ValueError as e:
            return 0

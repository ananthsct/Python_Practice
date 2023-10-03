class MathUtils:
    @staticmethod
    def square(x):
        return x * x

    @staticmethod
    def cube(x):
        return x ** 3

# Using static methods
result1 = MathUtils.square(5)  # No instance creation required
result2 = MathUtils.cube(3)

print(result1)  # 25
print(result2)  # 27

class MyClass:
    def __init__(self):
        self._my_attribute = 0

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        if value >= 0:
            self._my_attribute = value

myclass = MyClass()
print(myclass.my_attribute)
myclass.my_attribute = 50
print(myclass.my_attribute)

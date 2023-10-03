class MyClass:
    def __init__(self, my_variable):
        self._my_variable = my_variable

    #@property
    # def my_variable(self):
    #     return self._my_variable
    #
    # #@my_variable.setter
    # def my_variable(self, value):
    #     if value >= 0:
    #         self._my_variable = value
    #     else:
    #         print("Value must be non-negative")

    def __str__(self):
        return f'my variable is : {self._my_variable}'

obj = MyClass(42)
#print(obj.my_variable)  # Accessing via property
obj.my_variable = 30   # Setting via property
print(obj)
print(f'my variable is :{obj.my_variable}')

class A:
    def some_method(self):
        print("Method in class A")

class B(A):
    def some_method(self):
        print("Method in class B")

class C(A):
    def some_method(self):
        print("Method in class C")

class D(B, C):
    pass

d = D()
d.some_method()  # Output will follow the MRO: "Method in class B"
print(D.mro())   # Print the MRO for class D and its superclasses


def add(a, b):
    return a+b


class Animal:
    @staticmethod
    def lion():
        print("My name is lion")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def dog_age(self):
        print(f"Age of {self.name} is {self.age}")


if __name__ == "__main__":
    # Creating an instance of the Dog class
    my_dog = Dog("Buddy", 3)
    print(my_dog.name)  # Output: Buddy
    print(my_dog.age)
    my_dog.bark()       # Output: Buddy says Woof!
    my_dog.dog_age()        #

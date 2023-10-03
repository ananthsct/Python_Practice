import dog
from dog import *
from dog import Animal
from dog import Dog


dog2 = dog.Dog('Mani', 30)

dog2.bark()
dog2.dog_age()

x = dog.add(4, 5)
print(x)

y = add(9, 10)
print(y)

dog.Animal.lion()
animal = Animal()
animal.lion()
my_dog = Dog('jimmi', 12)
my_dog.bark()
my_dog.dog_age()

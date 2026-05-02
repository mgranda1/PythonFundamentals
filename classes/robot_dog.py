# Exploring classes
class Robot_Dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    def bark(self):
        print('Woof woof')

my_dog = Robot_Dog('Spot', 'Chihuahua')
print(f"{my_dog.name} {my_dog.breed}")
my_dog.bark()
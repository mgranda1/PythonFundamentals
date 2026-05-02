# Exporing class inheritance
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print(f"My name is {self.name}")

    def walk(self, x):
        self.position[0] += x
        print(f'New position: {self.position}')

    def eat(self):
        print("I'm hungry")

# Class inheritance
class Robot_Dog(Robot):
    def bark(self):
        print("Woof woof!")
    # Method override
    def eat(self):
        # Call parent class method
        super().eat()
        print("I like bacon")

def main():
    robot1 = Robot("Luna")
    robot1.walk(5)
    robot1.eat()

    robot2 = Robot_Dog("Azor")
    robot2.walk(2)
    robot2.bark()
    robot2.eat()

main()

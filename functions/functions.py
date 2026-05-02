# Discovering functions
# name variable is local to the function
def greeting(name):
    print(f"Hello {name}")

def addition(a,b):
    return a + b
    
def main():
    input_name = input("Enter your name: ")
    greeting(input_name)

    input_num1 = float(input("Enter first number: "))
    input_num2 = float(input("Enter second number: "))
    print(addition(input_num1, input_num2))

main()
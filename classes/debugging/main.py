from calc import add_numbers, divide_numbers
import random 

def main(value_param):
    a = 10
    b = random.randint(0,2)

    if value_param == 'sum':
        value = add_numbers(a, b)
        print(f"Adding {a} and {b}: {value}")
    
    if value_param == 'divide':
        value = divide_numbers(a, b)
        print(f"Dividing {a} and {b}: {value}")

if __name__ == "__main__":
    main('divide')
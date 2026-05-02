# Opening files
def find_acronym():
    acr = input("What software acronym would you like to look up? ")
    found = False

    # Opening file using with open() as file
    try:
        with open('./files_and_exceptions/input.txt') as file:
            for line in file:
                # Check if look_up is a substring of line
                if acr in line:
                    print(line)
                    found = True
                    break
            if not found:
                print("Acronym not found")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

def add_acronym():
    acr = input("What acronym you would want to add? ")
    definition = input("What is its definition? ")
    with open("./files_and_exceptions/input.txt", "a") as file:
        file.write(f"{acr} - {definition}\n")

def main():
    choice = input("Do you want to add acronym (A) or find acronym (F)")
    if choice == 'A':
        add_acronym()
    elif choice == 'F':
        find_acronym()
    else:
        print("Wrong input")
main()
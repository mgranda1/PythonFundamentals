# Exploring dictionary
acronyms = {'LOL': 'laugh out loud',
            'IDK': 'i don\'t know',
            'TBH': 'to be honest'}
try:
    key = 'BTW'
    print(acronyms['BTW'])
except:
    print(f"Exception has occured. Key {key} does not exist.")
finally:
    for k,v in acronyms.items():
        print(f"Acronym {k} stands for {v}")

def remainder_division(a,b):
    if b == 0:
        raise Exception('Divisor can not be 0')
    
    result = a//b
    remainder = a%b
    return print(f"Division result of {a} and {b}: ({result}, {remainder})")

remainder_division(2137,4)
# Exploring dictionary
acronyms = {'LOL': 'laugh out loud',
            'IDK': 'i don\'t know',
            'TBH': 'to be honest'}

print(acronyms['LOL'])

# Dictionary: unordered key:value pairs
dictionary = {}
dictionary['key1'] = 'first item'
dictionary['key2'] = 'second item'
dictionary['key3'] = 'third item'

key = 'LOL'
description = acronyms.get(key)
if description:
    print("Value of a key \'", key, '\' is', description)
else:
    print('Key doesn\'t exist')
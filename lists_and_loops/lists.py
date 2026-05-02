# List is a container with each of the items in order
#empty list
empty = []

# list of strings
words = ['LOL', 'IDK', 'TBH']

# list of numbers
numbers = [5, 10, 15]

# list of mixed items
mixed = [5, 'SDK', 1.5]

# list of lists
lists = [[1,2]]

# append to list
words.append("SMH") 
words.remove('TBH')

# remove from list
del words[0]

for word in words:
    print(word)

if "TBH" in words:
    print("TBH is in words list")
else:
    print("TBH is not in the words list")

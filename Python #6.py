'''
Lists

Lists are a data type in Python that let you group a bunch of data together

You create a list by using brackets [], you can put as much data in here as you want, even other variables!
The things inside a list are called 'items' or 'elements'.
List are zero-indexed (they start counting at 0)

Example)

brad_list = ['Brad', 24, 178.0]


Example)

name = 'Brad'
age = 24
height = 178.0

brad_list = [name, age, height]

'''


# Ex 1) Find the length of a list (the number of items in the list)

# len(list_name)

brad_list = ['Brad', 24, 178.0]
print(len(brad_list))



# Ex 2) Find the value at a certain position in a list (indexing)
# Find the age from the list (this is at position 1)

# list_name[pos]

brad_list = ['Brad', 24, 178.0]

print(brad_list[1])


# Ex 3) Use a slice to pull out multiple fruits from the list in a row (they must be next to eachother)

# list_name[start:end]    Note: the start is inclusive, end is exclusive

fruits = ['apple', 'banana', 'mango', 'orange', 'blueberries', 'strawberries', 'avocado']

print(fruits[2:5])


# Ex 4) If you dont put an end for the slice, it pulls out all the values for the rest of the list

# list_name[start:]

print(fruits[4:])


# Ex 5) If you dont put an start for the slice, it pulls out all the values from the start, up to the end value (but not including)

# list_name[:end]

print(fruits[:4])



# Exercises on your screen

brad_list = ['Brad', 'Smith', 24, 178.0, 'red', 'pizza', 'lobster', 'apple crumble']

print(brad_list) # Prints out the list

print(len(brad_list)) # Prints out the length of the list

print(brad_list[5]) # Prints 'pizza'

print(brad_list[1]) # Prints 'Smith'

print(brad_list[0]) # Prints 'Brad'

print(brad_list[4:7]) # ['red', 'pizza', 'lobster']

print(len(brad_list))

print(brad_list[0])

print(brad_list[4])

print(brad_list[7])

print(brad_list[2:5])

print(brad_list[2:])

print(brad_list[:5])

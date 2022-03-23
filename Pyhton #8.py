'''
# From Dawn_5.py

# Ex 5) Use a while loop to find the minimum value in a list of integer numbers
#       where all the number are only 1,2,3,4,5,6,7,8 or 9

numbers = [3,6,2,1,5,8,4,9]

count = 0
list_length = len(numbers)

min_value = 10

while count < list_length:
    if numbers[count] < min_value:
        min_value = numbers[count]
    count = count + 1

print('The minimum value is ' + str(min_value))



# Ex 6) Rewrite the code to find the maximum value instead of the minimum
numbers = [3,6,2,1,5,8,4,9]

count = 0
list_length = len(numbers)

max_value = 0

while count < list_length:
    if numbers[count] > max_value:
        max_value = numbers[count]
    count = count + 1

print('The maximum value is ' + str(max_value))




# A for loop iterates over a list or a string
# For loops have a counter built-in!
max_value = 0
for number in numbers:
    if number > max_value:
        max_value = number


min_value = 10
for number in numbers:
    if number < min_value:
        min_value = number

print('The minimum value is ' + str(min_value))
print('The maximum value is ' + str(max_value))

'''


names = ['Brad', 'Dawn', 'James', 'Bill', 'Tim', 'Jane']

# Print each name in a loop
for name in names:
    print(name)

# Print each initial
for name in names:
    print(name[0])

# Print each name in upper case
for name in names:
    print(name.upper())

# Print each name in lower case
for name in names:
    print(name.lower())


fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Strawberry', 'Avocado']

fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Strawberry', 'Avocado']

for fruit in fruits:
  print(fruit)
  
for fruit in fruits:
    print(fruit[0])
  
for fruit in fruits:
  print(fruit[4])
  
for fruit in fruits:
  print(fruit[-1])
  
for fruit in fruits:
  print(fruit.upper())
  
for fruit in fruits:
  print(fruit.lower())
  
for fruit in fruits:
  print(fruit.upper())
  print(fruit.lower())
  
for number in range(10):
    print(number)


# Using for loops with strings - not as common as for loops with lists but still useful
email_address = 'brad@email.com'
for char in email_address:
    print(char)



count = 0
while count < 50:
    print(count)
    count = count + 1

# we use range because for loops work with lists. range creates a list of numbers that starts from 0 and goes up to 1 before the number
# you pass in the parentheses. You can pass a start number if you dont want to start from 0
for number in range(50):
    print(number)

# the range function is useful because we can loop code a set number of times, we dont even have to use the 'number' variable!
for number in range(5):
    print('Hi')


for number in range(25, 51):
    print(number)

for number in range(10):
    print(number)

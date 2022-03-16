Roadmap
1) Data types and variables
2) Conditional statements (if, elif, else) - sometimes called 'Control Flow'

3) Loops <- we're here

4) Lists
5) Functions




----------- Loops -----------

What is a loop?
A loop is a way to repeat code over and over again until youre done

There are 2 kinds of loops in Python:
> While loops
> For loops

Why are there 2 kinds of loops:
> While loops - very old, can do everything, but they're a bit ugly
> For loops - newer, can do most things, but they're very good at what they do

'''

# Ex 1) For loops and While loops can do the same things most of the time
# x = 1
# while x < 6:
#     x += 1
#     print('Hi')

# for i in range(5):
#     print('Hi!')



'''
While loops

A while loop repeats code over and over again until a condition is met.
The loop only starts if the condition is True.
If it is True, run through the loop once
Check the condition again, if True, run through the loop again etc, if False stop
A while loop can run a known number of times AND an unknown number of times


Structure:

while <condition>:
    some
    code
    here

'''

# Ex 2) Write a program that checks every year if a person is old enough to drive.
#       When they're old enough, print "You can now drive" and stop checking their age
'''
age = 10
driving_limit = 18

while age < driving_limit:
    print('You are ' + str(age) + '. You are too young to drive.')
    age = age + 1 # increment (add 1)

print('You can now drive!')
'''


# Ex 3) WARNING: If you dont update the variable thats getting checked in the condition
#                you will get an infinite loop!

'''age = 10
driving_limit = 18

while age < driving_limit:
    print('You are ' + str(age) + '. You are too young to drive.')

print('You can now drive!')
'''

# Ex 4) Use a while loop to find the maximum value in a list of integer numbers
#       where all the number are only 1,2,3,4,5,6,7,8 or 9

numbers = [3,6,2,1,5,8,4,9]

count = 0
list_length = len(numbers) # get the length of the list of numbers

max_value = 0

while count < list_length:

    # numbers[count] means go to the list called 'numbers' and pull out the value at position 'count'
    if numbers[count] > max_value:
        max_value = numbers[count]
    count = count + 1

print('The maximum value is ' + str(max_value))


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


# Ex 6) Use a while loop to ask a user to enter their password, keep repeating until their password is correct
#       When the password is correct, print "Logged in successfully"

password = 'Password123'
user_input = ''

while user_input != password:
    user_input = input('Enter password: ')

print('Logged in successfully')
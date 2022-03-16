'''
Class 2 - Conditional Statements (if, elif, else)

Control Flow - the path your program takes

if      -   check if a condition evaluates to True
            Structure: if <condition>:
            To check equality use ==

elif    -   
else    -   


Comparison Operators - used to make comparisons between two values:

    ==  equality (has the same value)
    !=  not equal to (inequality)
    >   greater than
    <   less than
    >=  greather than or equal to 
    <=  less than or equal to

Logical Operators - used to chain together multiple conditions:

    and  returns True if all conditions are True
    or   returns True if at least one condition is True       
    not  returns True if the condition is False (the word swaps what the condition evaluates to)

'''

# Ex 1) Using strings
name = 'Brad'

if name == 'Brad':
    print('Hi Brad')


# Ex 2) Using integers - condition evaluates to True
x = 5
if x > 2:
    print('x is large')


# Ex 3) Using integers - condition evaluates to False
x = 5
if x > 20:
    print('x is really large!')


# Ex 4) If my_age is greater than or equal to drinking_age, print 'You can drink!'

drinking_age = 21
my_age = 18

if my_age >= drinking_age:
    print('You can drink!')


# Ex 5) A Zoo has a promotion, if you are exactly 50 years old, print 'You can enter for free!'
#       If the person is not exactly 50, print '$20 dollars please!'

age = 51

if age == 50:
    print('You can enter for free!')

if age != 50:
    print('$20 dollars please!')




'''

                   The difference between = and == :

=       assignment operator - use it to give a value to a variable

==      equality operator - use it to check if two values are the same

'''



# Ex 6) Using logical 'and' to check multiple conditions

is_raining = False
is_cold = True

if is_raining == True and is_cold == True:
    print('I dont want to go outside today!')


# Ex 7) Using logical 'or' to check multiple conditions
# Prints if at least one is True, if all are True then still print because at least one is True
# (it doesnt care how many are True)

is_raining = True
is_cold = False

if is_raining == True or is_cold == True:
    print('I dont want to go outside today!')



'''
In if statements that are made up of multiple conditions that are chained together,
everything between the 'if' and the ':' is the condition.

Example)

if is_raining == True or is_cold == True:
    print('I dont want to go outside today!')

In this code, the condition is: 'is_raining == True or is_cold == True'

'''

# Ex 8) Does this run? Yes! The condition is just 'True', 'True' evaluates to 'True' so it runs!

if True:
    print('This ran!')



# Ex 9) Does this run? Yes! Because 'is_raining' evaluates to 'True'!

is_raining = True

if is_raining:
    print('I dont want to go outside today!')


# Ex 10) Using logical 'not'

is_raining = True

if not is_raining:
    print('I will go outside!')



# Ex 11) not will flip True to False, which means the entire condition evaluates to False, so nothing prints

if not True:
    print('This will print!')



# Ex 12) 

dark_mode_enabled = True

if dark_mode_enabled:
    print('Dark mode is on')


if not dark_mode_enabled:
    print('Dark mode is off')


num=5
square = num * num
if square > 100:
    print('The square is large')

if square <= 100:
    print('The square is not large')
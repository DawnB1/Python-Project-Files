'''
Class 3 - Conditional Statements (if, elif, else)

Control Flow - the path your program takes

if      -   check if a condition evaluates to True
            Structure: if <condition>:
            To check equality use ==
            You can only have 1 if statement per if-else block
            You can have an if statement on its own

elif    -   
else    -   if none of the other conditions were met, run this code
            You can only have 1 if statement per if-else block
            You cant use an else statment on its own



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


# Ex 1) Write a program that calculates the price of a ticket to the zoo.
#       If the person is a senior citizen (age >= 55), they get a 20% discount
#       If not the ticket price is $20


age = 55
base_price = 20

# This is an if-else block

if age >= 55: # try this condition first, if True run the code and skip to the end of the if-else block
    ticket_price = 0.8 * base_price

else: # if the first condition was False, run this code
    ticket_price = base_price


print(ticket_price)


# Ex 2) A person rolls two dice, and takes the sum of the two rolls
#       If the sum is less than 6 print 'That was a bad roll'
#       If the sum was greater than or equal to 6 print that was a good roll

sum_of_rolls = 10

if sum_of_rolls < 6:
    print('That was a bad roll')

else:
    print('That was a good roll')



# Ex 3) Write a program to square a number. If the square is greater than 100, print 'The square is large'.
#       If the square is not greater than 100, print 'The square is not large'

num = 5
square = num * num



# Ex 4) Write a program that prints 'Hello' if the text is 'Hi', if the text is anything else print 'I only understand Hi'

text = 'Hi'

if text == 'Hi'

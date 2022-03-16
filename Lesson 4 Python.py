# Ex 2) A person rolls a di, 
#       If the number is 1, print 'You rolled a 1, how sad'
#       If the number is 2 'You rolled a 1, how sad'
#       If the number is 3 print '3 is about average'
#       If any other number is rolled print 'Good roll'

import random
number = random.randint(1,6)

if number == 1:
    print('You rolled a 1, how sad')

elif number == 2:
    print('You rolled a 2, a little better than 1 I guess')

elif number == 3:
    print('3 is about average')

else:
    print('Good roll')


# Ex 3) A person rolls a di
#       If the roll is even print 'Its even'
#       If the roll is odd print 'Its odd'
#       If the roll is 2 print 'This is a 2!' (dont print its even for this one)

# Hint: use modulo to help you (%) modulo gives you the remainder from a division
# 10 % 3 = 1
# 6 % 4 = 2
# 11 % 2 = 1
# 10 % 2 = 0

import random
number = random.randint(1,6)

# Note that the order is important! The program checks each statement in order, if one if True that code will run
# and no other statements will be checked! (even if they would also have been True)

# Its even
if number % 2 == 0:

# Its odd
elif number % 2 == 1:



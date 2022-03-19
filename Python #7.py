'''
Nested-Lists

A nested list is a list inside of another list

'''

brad_list = ['Brad', 
             'Smith', 
             24, 
             178.0, 
             'red', 
             'pizza', 
             'lobster', 
             'apple crumble'
             ]

employee_list = [
                    ['Forename', 'Surname', 'Salary', 'Email'],
                    ['John', 'Doe', 50_000, 'john.doe@email.com'],
                    ['Jane', 'Doe', 60_000, 'jane.doe@email.com'],
                    ['Joe', 'Bloggs', 50_000, 'joe.bloggs@email.com']                   
                ]

headers = employee_list[0]
john_list = employee_list[1]

print(john_list[3])

print(employee_list[1][3])

print(employee_list[2][2])



# Using square brackets to pull out a value from a list is called Indexing 
# The 'index' is the number that you type in the brackets

# brad_list[0]    this is the 0th index (the index is 0)
# brad_list[3]    this is the 3rd index (the index is 3)
# brad_list[5]    this is the 5th index (the index is 5)



# You can index strings too! This lets you pull out specific characters from a string

email = 'jane.doe@email.com'

print(email[4]) # Gets the .
print(email[8]) # Gets the @


# You can also use slices on strings!
print(email[2:6])



employee_list = [
                    ['Forename', 'Surname', 'Salary', 'Email'],
                    ['John', 'Doe', 50_000, 'john.doe@email.com'],
                    ['Jane', 'Doe', 60_000, 'jane.doe@email.com'],
                    ['Joe', 'Bloggs', 50_000, 'joe.bloggs@email.com']                   
                ]

# You can slice lists of lists
print(employee_list[1:])
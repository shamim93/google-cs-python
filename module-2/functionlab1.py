# Task 1
# Define a function named `alert()`

'''
def alert():
    print("Potential security issue. Investigate further.")

'''
# Task 2
'''
def alert():
    print("Potential security issue. Investigate further.")


alert()
'''

#  task 3
# The following code cell contains a variation of the alert() function that now uses a for loop to display the alert message multiple times.

'''
def alert():
    for i in range(3):
        print("Potential security issue. Investigate further.")


alert()

'''
# Task 4
'''
def list_to_string():
    usernameList = ['elarson', 'bmoreo', 'tshah', 'sglimore', 'eraab', 'dfjfs']
    for i in usernameList:
        print(i)


list_to_string()

'''


def list_to_string():
    usernameList = ['elarson', 'bmoreo', 'tshah', 'sglimore', 'eraab', 'dfjfs']
    sum_variable = ""
    for i in usernameList:
        sum_variable = sum_variable + i + ','
        newStr = sum_variable.rstrip(',')
        # print(newStr)
        # sum_variable = newStr

    print(newStr)


list_to_string()

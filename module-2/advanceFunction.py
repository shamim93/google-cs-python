# Arguments
def my_function(fname):
    print("Welcome " + fname)


'''
print("Enter customer's name: ")
firstName = input()
my_function(firstName)


'''
# Arbitrary Keyword Arguments, **kwargs

# user two * when you dont know how many parameters will be passed

'''

def newFunction(**fullname):
    print("Full name is " + fullname["llname"])


newFunction(ffname="Shamim", llname="Hossen")

'''

# default parameters

'''

def myCountry(country="Bangladesh"):
    print("I am from: " + country)


myCountry("Bangladesh")
myCountry("Poland")
myCountry("Austria")
myCountry("Cpublic")

'''

# passing a list as an arguments
'''

def myList(food):
    for i in food:
        print("The items are: " + i)


# fruits = ['apple', 'orange', 'banana']

# take list from user input
lst = []
userInput = int(input("Enter the number items: "))
for num in range(0, userInput):
    print("Enter the elements: ")
    newElement = input()
    lst.append(newElement)

myList(lst)
'''


#  return values

def sumOfTwo(num1, num2):
    return num1 + num2


inputValue = sumOfTwo(10, 20)
print(inputValue)

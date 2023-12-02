# Create a class named Person, use the __init__() function to assign values for name and age:

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# create object person class
p1 = Person("Shamim", 28)

print(p1.name)
print(p1.age)


'''
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


p1 = Person("Shamim", 28)
print(p1)

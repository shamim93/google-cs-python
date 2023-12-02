# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

# Insert a function that prints a greeting, and execute it on the p1 object:
    def objMethod(self):
        print("Hello", self.fname, self.lname)


p1 = Person("Shamim", "Hossen", 28)
p1.objMethod()

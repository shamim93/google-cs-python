'''
with open("test.txt", "a") as file:
    newLineAdd = file.write("\nNew text has been added to an existing file")
    file.close()
with open("test.txt", "r") as newf:
    newFile = newf.read()
print(newFile)
file.close()

'''

# creat a new file and write on it

with open("test2.txt", "w") as file:
    newFile = file.write("Hello World!")
    file.close()
with open("test2.txt", "r") as file:
    readFile = file.read()
print(readFile)

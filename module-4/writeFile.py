with open("test.txt", "a") as file:
    newLineAdd = file.write("\nNew text has been added to an existing file")
    file.close()
with open("test.txt", "r") as newf:
    newFile = newf.read()
print(newFile)
file.close()

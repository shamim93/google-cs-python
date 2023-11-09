# Specify the start index and the end index, separated by a colon, to return a part of the string.

print("Enter the string\n")
name = input()
print(name)


# get the character from the position 2 to 5

sliced_part = name[2:5]
print(sliced_part)

# Get the characters from the start to position 5 (not included):

startToEnd = name[:5]
print(startToEnd)

# Slice To the End
# By leaving out the end index, the range will go to the end:

indexToEnd = name[2:]
print(indexToEnd)

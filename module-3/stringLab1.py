# Task 1
# convert a number to string
# Assign `employee_id` to a four digit number as an initial value
'''

employee_id = 4186

# Display the data type of `employee_id`

print(type(employee_id))

# Reassign `employee_id` to the same value but in the form of a string

employee_id = str(employee_id)

# Display the data type of `employee_id` now

print(type(employee_id))


'''
# Task 2
#  Conditional statement to employee id,write a conditional statement that displays a message if the length of the employee ID is less than five digits.
'''
employee_id = 4186
print(type(employee_id))
employee_id = str(employee_id)

if len(employee_id) < 5:
    employee_id = employee_id + "E"

print(employee_id)
'''
# Task 5

# need to extract the first through the third characters in the device ID. So take a slice of the device ID.

# Assign `device_id` to a string that contains alphanumeric characters

device_id = "r262c36"

# Extract the first through the third characters in `device_id` and display the result

print(device_id[0:3])

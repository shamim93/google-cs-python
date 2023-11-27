# Task 2
# Append new items to list

'''
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]
# Assign `new_user` to the username of a new approved user
new_user = "gesparza"
# Assign `new_device` to the device ID of the new approved user
new_device = "3rcv4w6"
# Add that user's username and device ID to `approved_users` and `approved_devices` respectively
approved_users.append(new_user)
approved_devices.append(new_device)
# Display the contents of `approved_users`
print(approved_users)
# Diplay the contents of `approved_devices`
print(approved_devices)

'''
# Task 3
#  Remove users and devices from approved list

'''
approved_users = ["elarson", "bmoreno",
                  "tshah", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1",
                    "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]
removed_user = "tshah"
removed_device = "2ye3lzg"
approved_users.remove(removed_user)
approved_devices.remove(removed_device)
print(approved_users)
print(approved_devices)

'''

# Task 4
# Write a conditional statement that verifies if a given username is an element of the list of approved usernames.
'''
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
username = "shamim"

if username in approved_users:
    print("The username", username, "is approved to access the system.")
else:
    print("The user", username, "is not approved to access the system.")

    
'''
# Task 5
# The next part of the algorithm uses the .index() method to find the index of username in the approved_users and store that index in a variable named ind.
# When used on a list, the .index() method will return the position of the given value in the list.

'''
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
username = "sgilmore"
ind = approved_users.index(username)
print(ind)
'''
# Task 6
#  Get the index of the username and devices

'''
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
username = "sgilmore"
ind = approved_users.index(username)
# the devices of that index
assignedDevice = approved_devices[ind]
print(assignedDevice)

'''
# Task 7
# Conditional statement to compare approved devices and username
'''

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
username = "sgilmore"
device_id = "a307vir"
ind = approved_users.index(username)

# Conditional statement
# If `username` belongs to `approved_users`, and if the device ID at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device

if username in approved_users and device_id == approved_devices[ind]:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but",
          device_id, "is not their assigned device.")

'''

#  task 9
#  create a function to check username and assigned devices

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]


def login(username, device_id):
    if username in approved_users:
        print("The user", username, "is approved to access the system.")
        ind = approved_users.index(username)
        if device_id == approved_devices[ind]:
            print(device_id, "is the assigned device for", username)
        else:
            print(device_id, "is not their assigned device.")

    else:
        print("The username", username, "is not approved to access the system.")


login("bmoreno", "hl0s5o1")
login("bmoreno", "4n482ts")

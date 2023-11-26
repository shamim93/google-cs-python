# Task 2
# Append new items to list

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

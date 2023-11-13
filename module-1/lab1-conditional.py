# Assign `approved_list` to a list of approved usernames

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno"

# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours

organization_hours = True

# If the user is among the approved users and they are logging in during organization hours, then convey that the user is logged in
# Otherwise, convey that either the username is not approved or the login attempt was made outside of organization hours

if username in approved_list and organization_hours == True:
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")

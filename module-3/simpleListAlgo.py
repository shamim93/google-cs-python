IPaddr = ["198.223.xx.xx", "198.101.xx.xx", "180.064.xx.xx",
          "198.223.xx.xx", "192.168.xx.xx", "184.190.xx.xx"]
# Extract the first 3 characters from a list of IP address and assign to a new list with the first 3 characters

newIP = []
for address in IPaddr:
    firstThreeCharacters = address[0:3]
    # assign to a new list
    newIP.append(firstThreeCharacters)
    # print(firstThreeCharacters)
print(newIP)

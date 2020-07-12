# if statments
playerColor = "Green"
alienColors = ["green", "yellow", "red"]
if playerColor.lower() in alienColors:
    print(f"Player has 5 points")
playerColor = "red"
if playerColor.lower() == "green":
    print(f"Player has 5 points")
else:
    print(f"Player has 10 points")
playerColor = "Yellow"
if (playerColor.lower() == "green"):
    print(f"player has 5 points")
elif(playerColor.lower() == "yellow"):
    print(f"player has 10 points")
elif(playerColor.lower() == "red"):
    print(f"player has 15 points")

age = 25
if age < 2:
    print(f"person is a baby")
elif age >= 2 and age < 4:
    print(f"person is a toddler")
elif age >= 4 and age < 13:
    print(f"person is a kid")
elif age >= 13 and age < 20:
    print(f"person is a teenager")
elif age >= 20 and age < 65:
    print(f"person is a adult")
else:
    print(f"person is an elder")

# list based loops and conditionals
userRoles = ["admin", "developer", "power user", "user"]
if userRoles:
    for user in userRoles:
        if (user == "admin"):
            print(f"Hello {user}, Do you want to see a report")
        else:
            print(f"Hello {user}, Welcome")

# userRoles=[]
if userRoles:
    print(f"list is full")
else:
    print(f"list is empty")

requestedUserRoles = ["read only", "write only", "developer", "admin"]
for role in requestedUserRoles:
    if role in userRoles:
        print(f"Your requested role already exits")
    else:
        print(f"your requested role exists")

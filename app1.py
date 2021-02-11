#Storage program
print("Welcome to the vault")
who_user = input("Pick an user: ")

# Function that retrieves username's and passwords from storage
def keys():
    print(user_details[str(input("Enter a username or password to access: "))])


if who_user == #User real name (str):
    master_pass = input("Type the master password for this user: ")
    if master_pass == #Master password (str):
        username1 = input("Enter a username or email you want to store: ")
        password1 = input("Enter a password you want to store: ")
        access = input("Would you like to access a username or password? ")
        user_details = {# Call sign for actual username (str): #Enter an username (str),
                        # Call sign for actual password: #Enter a password (str),
        #Can expand for bigger storage
                        }
        if access == "yes":
            keys()
        if access == "no":
            print("Thank You for using this program")
    else:
        print("Fail, Restart program ")
else:
    print("Try again" + " " + who_user)
#Expandable if needed to add additional users
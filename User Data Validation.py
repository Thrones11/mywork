import re
import random
import string
import sys

keepAsking = True

contaner = []
user_data = []

while (keepAsking):
    First_name = input("Enter Firstname: ")
    Last_name = input("Enter Lastname: ")
    Email = input("Enter Email: ")

    user_data = ["The First name: " + First_name,
                 "The Last name: " + Last_name,
                 "Email: " + Email]
    contaner.append(user_data)


    def randomString(stringLength=5):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))


    def randomPassword():
        p = ("For suggested Password: " + First_name[:2] + randomString() + Last_name[-2:])
        print(p)


    randomPassword()

    msg = input("Enter Yes or No")
    if msg.lower() == 'yes' or msg.upper() == "YES":
        print("ok")

    else:
        msg.lower() == 'no' or msg.upper() == "No"
        while True:
            print ("""In the Password follow this: 
                   Total Character should be between 7 and 20
                   It should contain one letter between [a-z] 
                   It should contain one letter between [A-Z]
                   It should contain one letter between [0-9]
                   It should not contain any space""")
            p = input("Input your password:  ")
            is_valid = False

            if (len(p) < 7 or len(p) > 20):
                print("Not Valid1 Total Character should be between 7 and 20")
                continue

            elif not re.search("[a-z]", p):
                print("Not Valid! It should contain one letter between [a-z]")
                continue

            elif not re.search("[A-Z]", p):
                print("Not Valid! It should contain one letter between [A-Z]")
                continue

            elif not re.search("[0-9]", p):
                print("Not Valid! It should contain one letter between [0-9]")
                continue

            elif re.search("\s", p):
                print("Not Valid! It should not contain any space")
                continue
            else:
                is_valid = True
                break

            if is_valid:
                print("Password valid")

    doContinue = input("Continue? [y/n]  ")
    if doContinue.lower() == "y":
        keepAsking = True

    else:
        doContinue.lower() == "n"
        keepAsking = False

for contain in contaner:
    print("User details: ")
    print(contain)

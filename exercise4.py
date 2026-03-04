password = "python123"

user_input = input("Enter password: ")

while user_input != password:
    print("Wrong password. Try again.")
    user_input = input("Enter password: ")

print("Access Granted!")
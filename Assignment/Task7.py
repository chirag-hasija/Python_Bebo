preset_Username = "Chirag"
preset_Password = "654321"
username = input("Enter your username: ")
password = input("Enter your password: ")
if(username == preset_Username and password == preset_Password):
    print("Access granted")
else:
    print("Access denied")
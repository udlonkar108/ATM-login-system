
print("Welcome python ATM")

pin = int(input("Enter pin: "))
username = input("Enter username: ")
password = int(input("Enter password: "))

entered_pin = 3421
entered_username = "uday"
entered_password = 342108

if pin == entered_pin and username == entered_username and password == entered_password:
    print(" ATM Login successful")
elif pin != entered_pin and username != entered_username and password != entered_password:
    print("Wrong pin username and password")

elif pin != entered_pin and username != entered_username:
    print("Wrong pin and username")

elif pin != entered_pin and password != entered_password:
    print("Wrong pin and password")

elif username != entered_username and password != entered_password:
    print("Wrong username and password")

elif pin != entered_pin:
    print("Wrong pin")

elif username != entered_username:
    print("Wrong username")

else:
    print("Wrong password")

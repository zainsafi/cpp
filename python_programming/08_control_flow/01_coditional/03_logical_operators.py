# There are three Boolean or logical operators in Python: and, or, and not.
username = "admin"
password = "1234"
is_admin = False
account_active = True

if (username == "admin" and password == "1234") and (account_active or not is_admin):
    print("Access granted")
else:
    print("Access denied")
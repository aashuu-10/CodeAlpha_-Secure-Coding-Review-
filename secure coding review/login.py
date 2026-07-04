import hashlib
import getpass

USERNAME = "admin"

PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

if username == USERNAME and password_hash == PASSWORD_HASH:
    print("Login Successful")
else:
    print("Invalid Credentials")
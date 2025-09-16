import getpass
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Secure password input (hidden, not echoed)
password = getpass.getpass("Enter your password: ")

# Initialize Argon2 password hasher
ph = PasswordHasher()

# Hash the password securely (store only hash, never plaintext)
hashed = ph.hash(password)
print("Password received (hidden for security).")
print("Password hashed securely (store this):", hashed)

# Example verification (in real app, use stored hash)
try:
    ph.verify(hashed, password)
    print("Password verification successful")
except VerifyMismatchError:
    print("Invalid password")


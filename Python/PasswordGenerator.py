import random

all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567899876543210!#$%^&*()-_=+[{]}:<.>?|~'

def generate_password(length):
    generatedPassword = ''.join(random.sample(all_chars, length))
    return generatedPassword

password_length = 20 #int(input(\"Enter the password length: \"))
num_passwords = 10
for i in range(num_passwords):
    password = generate_password(password_length)
    print(f"Pass{i}: {password}")
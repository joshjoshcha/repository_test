# josh cha

def password_encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

  password = "12345555"
encoded_password = password_encoder(password)
print(encoded_password)  # prints "45678888"

password = "00009962"
encoded_password = password_encoder(password)
print(encoded_password)  # prints "33332295"

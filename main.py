# josh cha

def password_encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def password_decoder(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    option = input("Please enter an option: ")
    if option == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = password_encoder(password)
        print("Your password has been encoded and stored!")
    elif option == "2":
        decoded_password = password_decoder(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
    elif option == "3":
        brea

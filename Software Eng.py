
def password_encoder(password):
    string = ""
    for number in password:
        new_number = int(number) + 3
        string += str(new_number)
    return string

def password_decoder(new_password):
    new_string = ""
    for number in new_password:
        old_number = int(number) - 3
        new_string += str(old_number)
    return new_string

if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        print()
        options = int(input("Please enter an option: "))
        if options == 3:
            break
        if options == 1:
            password = input("Please enter your password to encode: ")
            new_password = password_encoder(password)
            print("Your password has been encoded and stored!")
            print()
        if options == 2:
            new = password_decoder(new_password)
            print(f"The encoded password is " +new_password+ ", and the original password is " +new+".")
            print()

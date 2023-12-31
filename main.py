#Dia Fallon and
#10/25/2023
#This program will take a user inputted password, encode it, and decode it

#Define encode function
def encode_password(user_password):
    #Initialize variables
    #string for encoded password
    encoded_password = ""
    #For character in user_password:
    for character in user_password:
        #Convert the character into an integer, add three to it, and convert it back to a string
        #Add the character to the encoded password string
        if int(character) < 7:
            encoded_password += str(int(character) + 3)
        else:
            encoded_password += str((int(character) + 3) - 10)
    #Return the encoded password
    return encoded_password


#Define decode function
def decode_password(password):
    decoded = ""
    for char in password:
        decoded += str((int(char)-3+10)%10)
    return decoded

#Define main function
def main():
    #Initialize variables
    #Int for menu choice
    menu_choice = 0
    #String for user password, encoded password, and decoded password
    user_password = encoded_password = decoded_password = ""
    while menu_choice != 3:
        #Print menu
        print("Menu"
              "\n-------------"
              "\n1. Encode"
              "\n2. Decode"
              "\n3. Quit\n")
        #Get user input for menu choice
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            #If user selects 1:
            #Get user input for 8 digit password
            user_password = input("Please enter your password to encode: ")
            #Invoke encode function
            encoded_password = encode_password(user_password)
            #Print that the password has been encoded and stored
            print("Your password has been encoded and stored!\n")
            # print(f"Encoded Password: {encoded_password}")
        #If the user selects 2:
        elif menu_choice == 2:
            #Invoke the decode function
            decoded_password = decode_password(encoded_password)

            #FIX ME: invoke the decode function, inputting the encoded password variable as a parameter,
            # and set the variable decoded_password equal to the output of the function

            #Print the encoded password and the original password
            print(f"The encoded password is {encoded_password}, and the decoded password is {decoded_password}\n")

        #If the user selects 3, quit
        elif menu_choice == 3:
            break

#Invoke Main
if __name__ == "__main__":
    main()
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
        encoded_password += str(int(character) + 3)
    #Return the encoded password
    return encoded_password

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
        #If the user selects 2:
        #Invoke the decode function
        #Print the encoded password and the original password
        #If the user selects 3, quit


#Invoke Main
if __name__ == "__main__":
    main()
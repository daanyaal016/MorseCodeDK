

file1 = open('codemorse.txt', 'w')
file1.write("A .- \nB  -...\nC -.-.  \nD -.. \nE .  \nF ..-. \nG  --. \nH  .... \nI .. \nJ .--- \nK -.- \nL .-.. \nM -- \nN -. \nO --- \nP .--. \nQ --.- \nR .-. \nS ... \nT - \nU ..-  \nV ...-  \nW .--  \nX -..-  \nY -.--  \nZ --..  \n1 .---- \n2 ..--- \n3 ...-- \n4 ....- \n5 .....  \n6 -.... \n7 --... \n8 ---.. \n9 ----. \n0 -----")
file1.close()
                 
def loadingofthedictionary(morseCodes):
    morseCodes = {}
    n = open("codemorse.txt")
    for line in n:
        key, value = line.split()
        morseCodes[key] = value

    return morseCodes


# function to convert normal text to morse code
def encryptionofnormaltext(message, morseCode):
    cipher = ''

    for letter in message:
        if letter != ' ':

            # Dictionary is looked up, and a space along with the corresponding morse code is added to separate 
            cipher += morseCode[letter] + ' '
        else:
            # to clarify 2 spaces specifys different words, and 1 space indicates a different characters
            cipher += ' '

    return cipher


# function that will convert morse code to English language
def decryptionofmorsecode(message, morseCode):
    message += ' '

    decipher = ''
    cipherText = ''

    for letter in message:
        # this will check for spaces 
        if letter != ' ':

            #this is a counter that will keep track of space
            spaceTrack = 0

            # morse code of a single character being stored
            cipherText += letter

        #if a space occurs
        else:
            # if spaceTrack = 1 this will indicate a new character
            spaceTrack += 1

            # A new word will be indicated if spaceTrack = 2 
            if spaceTrack == 2:

                # To separate words, adding a space
                decipher += ' '
            else:

                #reverse of encryption
                decipher += list(morseCode.keys())[list(morseCode.values()).index(cipherText)]
                cipherText = ''

    return decipher


# function to print menu
def printMenu():
    # All options available to the user
    print("Hello, this program allows you to translate text to morse code or translate morse code to text.")
    print()
    print("Please, select one of the below options:")
    print()
    print("*** Enter 't' for encoding text")
    print("*** Enter 'm' for decoding morse code")
    print("*** Enter 'e' to exit the program.")

    choice = input("\nMy input is: ")

    # A loop until the correct input is entered
    while True:
        if choice == 't' or choice == 'm' or choice == 'e':
            return choice
        else:
            print("***invalid option***")
            choice = input("Please enter a valid option: ")


#main(): this is a function for the main part of the program 
def main():
    # An empty dictionary is created here, to represent the morse code chart
    morseCodeDict = {}

    # have to call loadingofthedictionary(): function 
    morseCodeDict = loadingofthedictionary(morseCodeDict)

    while True:
        choice = printMenu()

        # if user enters 't'
        if choice == 't':
            text = input("\nPlease enter text to translate:\n")
            morse = encryptionofnormaltext(text.upper(), morseCodeDict)
            print(morse)
            print()

        # if user enters 'm'
        elif choice == 'm':
            morse = input("\nPlease enter morse to translate:\n")
            text = decryptionofmorsecode(morse.upper(), morseCodeDict)
            print(text)
            print()

        # if user enters 'e', exit the program
        else:
            print("\nThanks for using this program!\n")
            break

main()

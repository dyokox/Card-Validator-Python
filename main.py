import os
'''
This is a card validator. The way it works is
1. Get card number from user
2. Inverse it
3. Checks the card number length is valid
4. Every 2nd digit is doubled from right to left ←
5. If there are any digits bigger than 10, those two are added together (ex: 16 = 1 + 6 = 7) or subtract 9
6. With the new 'card number' add all the digits
7. sum % 10, if there is a remainder, then its invalid.
8. Print back to use if its valid or invalid
'''

evenDigits = 0
oddDigits = 0
totalDigits = 0

while True:
    cardInput = input("\n16 digit card (q to leave):\n >> ").lower()
    cardInput = cardInput.replace("-", "")
    cardInput = cardInput.replace(" ", "")
    cardInput = cardInput[::-1] 

    if cardInput == "q":
        break
    
    else:
        if len(cardInput) == 16:
            for i in cardInput[::2]:
                oddDigits += int(i)

            for i in cardInput[1::2]:
                i = int(i) * 2
                if i >= 10:
                    evenDigits -= 9
                else: 
                    evenDigits += i

            totalDigits = evenDigits + oddDigits
            if totalDigits % 10 == 0:
                print("Valid")
            else:
                print("Invalid") 

        elif len(cardInput) < 16 or len(cardInput) > 16:
            print("\nCard length invalid. Card numbers are 16 digits. Try again")

        else:
            print("Invalid input, try again\n")


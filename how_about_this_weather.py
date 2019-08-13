def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not a valid ZIP code in XXXXX format! Try again!")
            continue
        else:
            return userInput
            break

###MAIN
Zip = inputNumber("Enter 5-digit U.S. ZIP code for FREE and SEMI-ACCURATE weather: ")
from pprint import pprint
import zipcodes
zipCode = (str(Zip))
print(zipCode)
pprint(zipcodes.matching(zipCode))



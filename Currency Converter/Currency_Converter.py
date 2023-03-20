
# Notes for future: 
# - Put currency type and conversion rate in a list so they can be edited (added to or removed from)
# Code staff options area


def LineBreak(): # Adds a line break in
  print("\n------------------------------\n")

def ConversionRate(sCurrancyType): # Supplies the conversion rate for a currency when asked
  if sCurrancyType == "USD" or sCurrancyType == "usd":
    return 1.40
  elif sCurrancyType == "EUR" or sCurrancyType == "eur":
    return 1.14
  elif sCurrancyType == "BRL" or sCurrancyType == "brl":
    return 4.77
  elif sCurrancyType == "JPY" or sCurrancyType == "jpy":
    return 151.05
  elif sCurrancyType == "TRL" or sCurrancyType == "trl":
    return 5.68

def TransactionFees(iGBP):  
  if iGBP < 300: # Calculates the transaction fees for the conversion
    return iGBP * 0.035
  elif iGBP >= 300 and iGBP < 750:
    return  iGBP * 0.03
  elif iGBP >= 750 and iGBP < 1000:
    return iGBP * 0.025
  elif iGBP >= 1000 and iGBP < 2000:
    return iGBP * 0.02
  elif iGBP >= 2000:
    return iGBP * 0.015

# Enter the amount in £ that the customer wishes to convert
print("----------Start----------\n")
print("Welcome to the currency converter!")

bContinue = True

while bContinue:
  print("1: Convert GBP")
  print("2: Staff options")
  print("3: Exit the program")
  
  sUserInput = input("Please select an option: ") # Asks the user to choose an option

  if sUserInput == "1": # User chooses to convert GBP

    LineBreak()
    
    iGBP = int(input("Please enter the amount of GBP you wish to convert: "))
    
    if iGBP > 2500: # If the GBP is >2500, print message and go back to start of loop
      print("\nI'm sorry, there is a £2500 limit on currancy conversions, please enter a smaller amount.\n")
      continue
      
    else:
      sCurrancyType = input("""\nPlease enter the currancy you wish to convert to:\n
USD = American Dollars
EUR = Euros
BRL = Brazilian Real
JPY = Japanese Yen
TRL = Turkish Lira
----> """)
      
      iConvertedCurrancy = round((iGBP * ConversionRate(sCurrancyType)), 2) # Calls the function and sends CurrancyType to it, then returns the correct rate and calculates the amount of new currancy obtained, rounded to 2 decimal places
      sStaffDiscount = input("\nIs there a staff discount? Y/N: ")
      
      iTotalCost = round(iGBP + TransactionFees(iGBP)) # Calls the TransactionFees function and adds it to the GBP

      if sStaffDiscount == "Y" or sStaffDiscount == "y":
        iStaffDiscount = round((iTotalCost * 0.05), 2)
      else:
        iStaffDiscount = 0
      # If there is a staff discount, calculate it and round to 2 decimal places. If not, set it to 0
      LineBreak()
      
      print("Here is your conversion breakdown: ")
      print("Converted Currency: " + str(iConvertedCurrancy) + " " + sCurrancyType.upper())
      print("Transaction Fee: £"+ str(TransactionFees(iGBP)))
      print("Discount: £" + str(iStaffDiscount))
      print("Total Cost: £" + str((iTotalCost - iStaffDiscount)))
      # Print the conversion breakdown, converting the integers to strings so they can be concatinated

      input("\nThank you! To go back to the begining, enter any key: ")
      
      LineBreak()

  elif sUserInput == "2":

    LineBreak()
    
    print("Welcome to the staff option page, where you heave the options of changing the currency conversion rates, removing currencies and adding currencies.\n")
    print("1: Change the rate of conversion for a currency")
    print("2: Add a currency")
    print("3: Remove a currency")
    print("4: Go back to previous menu\n")

    sUserInput = input("Please select an option: ")
    
    if sUserInput == "1":
      asdasd

    elif sUserInput == "2":
      asdasdsd

    elif sUserInput == "3":
      asdasdsd

    elif sUserInput == "4":
      continue
  
  elif sUserInput == "3": # User chooses to exit the program

    LineBreak()
    
    print("Thank you for using the program\n")
    bContinue = False
  

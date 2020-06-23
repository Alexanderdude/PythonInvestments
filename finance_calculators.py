import math  # Imports the math module


print("\n" + "Choose either 'investment' or 'bond' from the menu below to proceed: " + "\n" + "\n" +
      "investment \t - to calculate the amount of interest you'll earn on interest" + "\n" +
      "bond \t \t - to calculate the amount you'll have to pay on a home loan")   # Displays text for the user


sType = input("\n" + "Please enter your answer here: ")   # Gets the users input 
sType = sType.upper()   # Makes the input all in capital letters

print("\n")




if sType == "INVESTMENT" :  # If the user entered investment

    rOriginal = float(input("\n" + "Please enter the amount of money you are depositing: "))  # User input

    rInRate = float(input("\n" + "Please enter the interest rate: "))  # User input

    iYears = int(input("\n" + "Please enter the amount of years the money will be deposited: "))  # User input

    sInType = input("\n" + "Will it be compound or simple interest?: ")  # User input
    sInType = sInType.upper() # Makes the input all in capital letters
    



    if sInType == "SIMPLE" :  # If user typed simple

        rTotal = rOriginal * (1 + ((rInRate / 100) * iYears))

        print("\n \n" + "Wow, you will start off with R" + str(rOriginal) + " and after " +  str(iYears) +
              " years you will get a total of R" + str(rTotal) + ". That is a R" + str(rTotal - rOriginal)
              + " increase!" )
        



    elif sInType == "COMPOUND" :   # If user typed compound

        rTotal = rOriginal * ((1 + (rInRate / 100))) ** iYears   # Compound interest formulae

        print("\n \n" + "Wow, you will start off with R" + str(rOriginal) + " and after " +  str(iYears) +
              " years you will get a total of R" + str(rTotal) + ". That is a R" + str(rTotal - rOriginal)
              + " increase!" )




    else :

        print("\n \n" + "Please select either 'simple' or 'compound' ")   # Error message





elif sType == "BOND" :

    rVal = float(input("\n" + "Please enter the value of your house: ")) # User input

    rInRate = float(input("\n" + "Please enter the interest rate: ")) # User input

    iMonth = int(input("\n" + "Please enter the number of months you want to take to repay the bond: ")) # User input


    rTotal = (((rInRate / 100) / 12) * rVal)/(1 - ((1 + ((rInRate / 100) / 12)) ** (-iMonth)))  # bond interest formulae


    print("\n \n" + "You will have to pay R" + str(rTotal) + " each month for a total of " + str(iMonth) + " months.")


else :

    print("\n \n" + "Please select either 'bond' or 'interest' ")   # Error message
    


    

































    
        

        


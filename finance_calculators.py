# Step 1: Get investment type
investment_type = input("Please enter 'bond' or 'investment': ")
if investment_type.casefold() not in ['bond', 'investment']:
    print("Error: Invalid selection. Please enter either 'bond' or 'investment'.")
else:
    # Step 2: investment type is valid
    if investment_type.casefold() == 'investment':
        try:
            amount = int(input("Enter the amount you are depositing: "))
            interest_rate = float(input("Enter the interest rate (as a percentage): "))
            years = int(input("Enter the number of years you plan on investing: "))
            interest = input("Do you want 'simple' or 'compound' interest? ").lower()

            if interest not in ['simple', 'compound']:
                print("Error: Invalid interest type. Please enter either 'simple' or 'compound'.")
            else:
                # Step 3: Calculate returns based on selected type of interest
                if interest == 'simple':
                    total_amount = amount * (1 + (interest_rate / 100) * years)
                    print(f"The interest earned after {years} years with simple interest will be: ${total_amount - amount:.2f}")
                
                elif interest == 'compound':
                    total_amount = amount * ((1 + (interest_rate / 100)) ** years)
                    print(f"The interest earned after {years} years with compound interest will be: ${total_amount - amount:.2f}")

        except ValueError:
            print("Error: Please enter valid numeric values.")

    # Bond calulation below:
        
    elif investment_type.casefold() == 'bond':
        try:
            amount = int(input("The present value of the house: "))
            interest_rate = float(input("The interest rate (as a percentage): "))
            interest_rate = (interest_rate / 100) / 12
            years = int(input("The number of months they plan to take to repay the bond: "))
            repayment = (interest_rate * amount)/(1 - (1 + interest_rate)**(-years))
            print("This is your monthly repayment: ", round(repayment, 2))

        except ValueError:
            print("Error: Please enter valid numeric values.")

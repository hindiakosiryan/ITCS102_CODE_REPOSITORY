age = int(input("Enter your age: "))
is_employed = bool(input("Are you employed? (True/False): "))
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
has_collateral = bool(input("Do you have collateral? (True/False): "))

if age >= 21 and is_employed:
    print("You are eligible for the loan.")
    #tier1
    if credit_score >= 750:
        print("You have a good credit score.")
        if annual_income >= 100000:
            base_rate = 4.5
            print("You have a high income. Your interest rate is 4.5%." )
        else: 
            base_rate = 5.0
            print("You have a moderate income. Your interest rate is 5%." )
            #Tier2
            if credit_score <= 750:
                base_rate = 8.0
                print("You have a low credit score. Your interest rate is 8%." )
                if annual_income < 40000:
                    base_rate = 9.5
                    print("You have a low income. Your interest rate is 9.5%." )
                    #Tier3
                    if credit_score < 600:
                        base_rate = 7.0
                        print("Rejected: Your credit score is too low for a loan.")        
                    else:
                        print("You have a moderate credit score. Your interest rate is 7%." )    
    else:
        print("You have a low credit score.")
    
else:
    print("You are not eligible for the loan.")

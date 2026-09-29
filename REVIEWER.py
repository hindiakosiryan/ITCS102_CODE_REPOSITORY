age = int(input("Enter Age: ---> "))
monthly_rev = float(input("Your Monthly Revenue: ---> "))
credit_score = int(input("Credit Score: ---> "))
years_in_business = int(input("Years in Business: ---> "))
defaults = bool(input("Has defaults: ---> "))
collateral = str(input("Name of the collateral: ---> "))
collateral_value = float(input("Collateral Value: ---> "))

max_loan = 0
base_fee = 0

if age >= 21 and years_in_business >= 2.0 and defaults == False:
    print("ELIGIBLE FOR THE LOAN")
    #TIER1
    if credit_score >= 720:
         
         max_loan = 3 * monthly_rev
         if monthly_rev >= 50000:
             print("MAX LOAN GREATER THAN", max_loan)
             base_fee = max_loan * 1.5
             print("BASE FEE IS SET TO", base_fee)
         else:
             base_fee = max_loan * 0.025
             print("BASE FEE IS SET TO", base_fee)
         if collateral_value >= max_loan:
             print("ACCEPTED")
         else: 
             print("REJECTED: INSUFFICIENT FUND FOR", collateral_value)
        #SURCHARGE
         surcharge_fee_rate = max_loan * base_fee
         if surcharge_fee_rate % 5000 != 0:
             base_fee += 250
             print("SURCHARGE FEE RATE:", base_fee)


    
    #TIER 2
    elif 620 <= credit_score < 720:

        max_loan = 1.5 * monthly_rev
        print("MAX LOAN GREATER THAN", max_loan)
        if years_in_business >= 5.0:
            base_fee = max_loan * 0.02
            print("BASE FEE RATE IS SET TO:", base_fee)
        else: 
            base_fee = max_loan * 0.035
            print("BASE FEE RATE IS SET TO:", base_fee)
        if collateral_value >= max_loan:
                         print("ACCEPTED")
        else: 
                         print("REJECTED: INSUFFICIENT FUND FOR", collateral_value)
        #SURCHARGE
        surcharge_fee_rate = max_loan * base_fee
        if surcharge_fee_rate % 5000 != 0:
         base_fee += 250
        print("SURCHARGE FEE RATE:", base_fee)
            
            
    #TIER3
    elif credit_score < 620:
        print("CREDIT SCORE TOO LOW")

    else: 
        print("NOT ENOUGH CREDIT SCORE")
else:
    print("NOT ELIGIBLE FOR THE LOAN")

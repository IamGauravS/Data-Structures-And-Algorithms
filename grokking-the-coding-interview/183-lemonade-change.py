def lemonade_change(bill):
    no_of_5_dollar_bill = 0
    no_of_10_dollar_bill = 0
    
    for b in bill:
        if b == 5:
            no_of_5_dollar_bill += 1
            
        elif b == 10:
            if no_of_5_dollar_bill == 0:
                return False 
            no_of_5_dollar_bill -= 1
            no_of_10_dollar_bill += 1
            
        elif b == 20:
            if no_of_10_dollar_bill > 0 and no_of_5_dollar_bill > 0:
                no_of_10_dollar_bill -= 1
                no_of_5_dollar_bill -= 1
            elif no_of_5_dollar_bill >= 3:
                no_of_5_dollar_bill -= 3
            else:
                return False 
    return True
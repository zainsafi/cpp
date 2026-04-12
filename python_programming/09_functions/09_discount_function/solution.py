# Calculating discount function with two arguments passed

def apply_discount(price,discount):
    # if type(price) != int and type(price) != float: or
    if not isinstance(price,(int,float)): # best way
        return "The price should be a number"
    
    # if type(discount) != int and type(discount) != float: or
    if not isinstance(discount,(int,float)):
        return "The discount should be a number"      

    if price <= 0:
        return "The price should be greater than 0"
        
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calculate final price
    final_price = price * (1 - discount / 100)   
    return final_price

print(apply_discount(1000,10))
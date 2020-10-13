def shop():
    print ("---------------------------------------------------")
    print ("Next Customer")
    print ("-----")
    spend = int (input ("Customer spend: "))
    
    if spend > 150:
        np = spend * 0.8
        print ("Discount Issued, New Price: ")
        print (np)
        print ("Ammount Saved: ")
        print (spend - np)
        shop()
    
    elif spend < 0:
        print ("Error, price cannot be less than 0")
        shop()
    
    else:
        print ("No Discount")
        shop()

shop()

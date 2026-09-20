#7. Best Time to Buy and Sell Stock
def ByAndSellStock(l):
    
    buy=l[0]
    Maxmargin=0
    for x in l:
        if x<buy:
            buy=x
        else:
            margin=x-buy
            if margin>Maxmargin:
                Maxmargin=margin
    return Maxmargin
    
prices = [7, 1, 5, 3, 6, 4]
print(ByAndSellStock(prices))
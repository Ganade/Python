# Make an algorithm that reads the price of a product and displays its new price, with a 5% discount.

price = float(input("Enter the value of the product to apply the discount: "))  # read the price of the item
discount = 5    # value of the discount to be applied
price_discount = price - (price/100)*discount   # calculate the price of the item with the discount
print(f"The price of the product is {price}, with the discount it will be {price_discount:.4}")

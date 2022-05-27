# Make an algorithm that reads the price of a product and displays its new price, with a 5% discount.

price = float(input("Enter the value of the product to apply the discount: "))
discount = 5
price_discount = price - (price/100)*discount
print(f"The price of the product is {price}, with the discount it will be {price_discount:.4}")

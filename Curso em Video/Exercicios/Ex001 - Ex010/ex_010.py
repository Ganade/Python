# Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.

wallet = float(input("How much money do you have in your wallet?: "))   # read the value that you have on wallet
dolar = 4.77    # value of dollar
print(f"You can by {wallet/dolar:.4} dolars")   # shows how many dollars you can buy with the amount you have in your wallet

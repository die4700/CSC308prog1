#Dietz Kiger Lytle

name = input("Please enter your name: ")
boughtShares = input("Enter the number of shares purchased: ")
purchasedPer = input("Enter the amount payed per share: $")
commission = input("Enter the commission paid (percent): ")

boughtSub = (float(boughtShares) * float(purchasedPer))
brokerBought = boughtSub * (float(commission) / 100)
boughtTotal = (boughtSub - brokerBought)

soldShares = input("Enter the number of shares sold: ")
soldPer = input("Enter the amount each share sold for: $")

soldSub = (float(soldShares) * float(soldPer))
brokerSold = (soldSub * (float(commission) / 100))
soldTotal = (soldSub - brokerSold)
profit = (soldTotal - boughtTotal)

print(name, "bought", boughtShares, "shares for $", purchasedPer, "per share.")
print("Gross Purchase: $", boughtSub, "\nCommission: $", brokerBought, "\nNet Purchase: $", boughtTotal)
print(name, "sold", soldShares, "shares for $", soldPer, "per share.")
print("Gross Sale: $", soldSub, "\nCommission: $", brokerSold, "\nNet Sale: $", soldTotal)
print(name, "made a profit of: $", profit)
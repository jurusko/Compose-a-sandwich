#! python3
# sandwich.py - Compose a sandwich and pay the price.
import pyinputplus as pyip

priceList = {"white" : 0.99, "brown" : 1.29, "sourdough" : 1.49,
             "chicken" : 2.99, "ham" : 2.99, "tofu" : 3.99,
             "cheddar" : 2.99, "mozarella" : 3.19, "podlaski" : 0.12,
             "tomato" : 2.00, "mayo" : 2.30, "spicy" : 2.40}

# Summarize price for one item.
def totalprice(menu, order):
    price_sum = 0
    for k, v in order.items():
        price_sum = price_sum + menu.get(k)

# Print a receipt.
def printReceipt(itemsDict, leftWidth, rightWidth):
    print("\n\n")
    print("McJuras Ltd".center(leftWidth + rightWidth, ' '))
    print("Fiscal receipt".center(leftWidth + rightWidth, ' '), end='\n')
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ' ') + str(v).rjust(rightWidth)) # Print chosen ingredients.
    print("Amount".ljust(leftWidth, ' ') + str(howMany).rjust(rightWidth)) # Print the amount.
    print("\nTOTAL PLN".ljust(leftWidth, ' ') + "%s".rjust(rightWidth-2) % (receipt)) # Print the price.
    print("\n")
    print("Thank you and see you soon!".center(leftWidth + rightWidth, ' '))

# Empty dict for customer order.
yourOrder = {}

# Order start.
print("Welcome to McJuras! You can try my delicious sandwiches. Please tell me, which type of bread you prefer?")
bread = pyip.inputMenu(['white', 'brown', 'sourdough'])
yourOrder[bread] = priceList.get(bread) # Choose bread type.

protein = pyip.inputMenu(['chicken', 'ham', 'tofu'])
yourOrder[protein] = priceList.get(protein) # Choose protein type.

print("Do you want cheese? (Y/N)")
cheeseQuestion = pyip.inputYesNo() # Ask for cheese.
if cheeseQuestion == "yes":
    cheeseType = pyip.inputMenu(['cheddar', 'mozzarella', 'podlaski'])
    yourOrder[cheeseType] = priceList.get(cheeseType)  # Choose cheese type.
    print("Double? (Y/N)")
    doubleCheeseQuestion = pyip.inputYesNo() # Ask for double cheese.
    yourOrder[cheeseType] = priceList.get(cheeseType) * 2
else:
    print("On a diet?")
    print("")

print("Any sauce? (Y/N)")
dressingQuestion = pyip.inputYesNo() # Ask for dressing.
if dressingQuestion == "yes":
    print("What sauce to add?")
    dressingType = pyip.inputMenu(['tomato', 'mayo', 'spicy'])
    yourOrder[dressingType] = priceList.get(dressingType)  # Choose dressing type.
else:
    print("Are you sure? Never mind.")
    print("")

print("How many sandwiches?")
howMany = pyip.inputInt() # Asks for how many sandwiches.

price = totalprice(priceList, yourOrder)

receipt = f"{howMany * sum(yourOrder.values()):.2f}" # Total price for sandwich(es).
print("In total is going to be %s " % (receipt) + "PLN.")

print("Do you need a receipt? (Y/N)")
receiptQuestion = pyip.inputYesNo() # Asks to show the receipt.
if receiptQuestion == "yes":
    printReceipt(yourOrder, 20, 20)
else:
    print("Good. ECO friendly :)")
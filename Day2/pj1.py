print("Welcome to the tip calculator  !")
totol_bill = float(input("What was the total bill? $"))
bill_percentage = float(input("What percentage tip wolud you like to give? 10, 12 or 20"))
person = int(input("How many people to split the bill? "))
final = "{:.2f}".format((totol_bill  * (1 + (bill_percentage/100)))/person)
print(f'Each person should pay: ${final}')


print("Welcome to tip calculator!")
cost=input("Enter the total cost:")
people=input("Enter the number of people:")
print("Cost per head:")
cph=(float(cost)/int(people))*1.12
print("%.2f" % cph)
#%.2f gives us 2 decimal places
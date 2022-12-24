age = input("What is your current age? ")
year_int=int(age)
years=90-year_int
months=(years*12)
weeks=(years*52)
days=(years*365)
msg=f"You have {days} days, {weeks} weeks, and {months} months left."
print(msg)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#Write your code below this line 👇
bmi=int(weight)/float(height)**2
#to make sure the final bmi value is an integer value and not a float we use type casting
print(int(bmi))
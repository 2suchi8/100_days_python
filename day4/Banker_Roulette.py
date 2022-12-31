import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num=len(names)
i=random.randint(0,num-1)
person_who_is_going_to_pay=names[i]
print(person_who_is_going_to_pay,"is going to buy the meal today!")
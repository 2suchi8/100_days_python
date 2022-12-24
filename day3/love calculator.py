print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
l_name1=name1.lower()
l_name2=name2.lower()
comb=l_name1+l_name2
ct=comb.count('t')    #ct=count t
cr=comb.count('r')    #cr=count r and so on for true and love
cu=comb.count('u')
ce=comb.count('e')
true=ct+cu+ce+cr
cl=comb.count('l')
co=comb.count('o')
cv=comb.count('v')
ce=comb.count('e')
love=cl+co+cv+ce
score=str(true)+str(love)
ii=int(score)
if(ii<10 or ii>90):
    print("Your score is "+score+", you go together like coke and mentos.")
elif(ii>=40 and ii<=50):
    print("Your score is "+ score+", you are alright together.")
else:
    print("Your score is "+ score +".")



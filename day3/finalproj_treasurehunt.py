print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Let us begin.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print("Your reach a forking path. Which side do you choose? Left or Right?:")
#lr=left or right
lr=input()
if(lr=='Left'):
  print("Continue. You walk through the dark woods and hear a sound. It-It sounds like a stream! You follow it. However your path is blocked by the gushing stream.What would you do? Swim or wait?")
  #sw= swim or wait
  sw=input()
  if(sw=='Wait'):
    print("You wait for the stream to calm down. You sit on a nearby rock and look round, enjoying the sound of water flowing over the rocks and the birds chirping. The sun is warm on your face. Something catches your eye. It is a hidden door! It leads you to a corridor full of doors of different colours. Red, yellow..blue, you name it!Which door do you choose?")
    #door= door colour
    door=input()
    if(door=="Red"):
      print("Burned by fire. Game over.")
    elif(door=="Blue"):
      print("Eaten by beasts. Game over.")
    elif(door=='Yellow'):
      print("You win!")
    else:
      print("Game over.")
  elif(sw=='Swim'):
    print("Attacked by trout. Game over.")
elif(lr=='Right'):
  print("Fall into a hole. Game over.")
    

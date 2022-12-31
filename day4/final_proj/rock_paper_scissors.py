import random
print("Welcome to rock paper scissors! Let us begin!")
rps=["Rock","Paper","Scissors"]
print("Player 1 input is:")
player1=random.choice(rps)
print(player1)
print("Player 2 input is:")
player2=random.choice(rps)
print(player2)
if(player1==player2):
  print("Tie. Play again.")
elif(player1=='Scissors' and player2=='Rock'):
  print("Player 2 wins")
elif(player1=='Paper' and player2=='Rock'):
  print("Player 1 wins")
elif(player1=='Scissors' and player2=='Paper'):
  print("Player 1 wins")
elif(player1=='Rock' and player2=='Paper'):
  print("Player 2 wins")
elif(player1=='Rock' and player2=='Scissors'):
  print("Player 1 wins")
elif(player1=='Paper' and player2=='Scissors'):
  print("Player 2 wins")
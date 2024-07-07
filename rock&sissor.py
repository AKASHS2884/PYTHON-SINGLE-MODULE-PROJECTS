import random

user_win=0
computer_win=0
options=["rock","paper","sissor"]

while True:
     user_input = input("type rock/paper/sissor or q to quit:").lower()
     if user_input == "q":
       break
       
     if user_input not in options:
      continue
    
    
random_number = random.randint(0,2)
#rock=0,paper=1,sissor=2

computer_pick = options[random_number]
print("computer_chooses",computer_pick +".") 

# conditions
if user_input=="rock" and computer_pick=="paper":
      print("YOU WON THE GAME")
      user_win+=1
elif user_input=="paper" and computer_pick =="sissor":
      print("YOU WON THE GAME")
      user_win+=1
elif user_input=="sissor" and computer_pick=="rock":
      print("YOU WON THE GAME")
      user_win+=1
else:
      print("you lost and computer won the game")
      computer_win+=1
      
      print("YOU WON",user_win,"TIMES.")
      print("COMPUTER WON",computer_win,"TIMES.")
      

print("GOOD BYE")
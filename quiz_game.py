print("welcome to the quiz game by akash")
playing=input("Do you want to play the game?:")
if playing!="yes":
    quit()
    
print("lets play the game :)")
score=0
##### answer segments for the quiz game ###
### 1 ### 
answer=input("when did india got independance?")
if answer=="1947":
    print("you are correct :)")
    score +=1
else:
    print("you are wrong,better luck next time :(")
    
### 2 ###   
answer=input("what is cpu?")
if answer.lower()=="central processing unit": ### .lower()- convert any case into lower case ###
    print("you are correct :)")
    score +=1
else:
    print("you are wrong,better luck next time :(")
### 3 ###      
answer=input("how many states are there in india?")
if answer=="28":
    print("you are correct :)")
    score +=1
else:
    print("you are wrong,better luck next time :(")
### 4 ###     
answer=input("who is the father of computer?")
if answer.lower()=="charles babbage": ### .lower()- convert any case into lower case ###
    print("you are correct :)")
    score +=1
else:
    print("you are wrong,better luck next time :(")
### 5 ###     
answer=input("who contribute for invention of bulb with edison?")
if answer.lower()=="tesla": ### .lower()- convert any case into lower case ###
    print("you are correct :)")
    score +=1
else:
    print("you are wrong,better luck next time :(")
    
### result ####
print("YOU GOT " + str(score) +"no. of questions correct")
print("YOU GOT " + str((score/5)*100) +"%")
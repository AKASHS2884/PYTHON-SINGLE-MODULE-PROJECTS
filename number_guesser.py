import random
top_of_range = input("ENTER THE NUMBER YOU GUESS? :")
guesses =0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("ENTER THE NUMBER GREATER THAN 0, NEXT TIME :(")
        quit()
else:
   print("ENTER THE NUMBER DIGIT, NEXT TIME :(")
   quit()
   
random_number=random.randint(0,top_of_range)

while True:
    guesses += 1
    user_guess = input("MAKE A GUESS? ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
         print("ENTER THE NUMBER DIGIT, NEXT TIME :(")
         continue
   
  
    if user_guess == random_number:   
       print("YOU ARE RIGHT")
       break
   
else:
    print("YOU ARE WRONG")
       
print("YOU GOT IN"+ guesses + "guesses")
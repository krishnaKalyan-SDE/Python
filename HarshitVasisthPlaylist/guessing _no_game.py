Guessed_no=int(input("Enter no:"))
import random
winning_no=random.randint(1,100)
if winning_no==Guessed_no:
     print(f"You guessed perfect no{Guessed_no}")
     print(f"Winning_no was {Guessed_no},CONGRATS YOU WON!!!")
else:
     if winning_no>Guessed_no:
          print("too low")
     else :
          print("too high")


     

import random

print("program execution start")

items = ["R", "P", "S"]

while True:
  player_choice = input("Enter your choice from this options -> R, P, S: ")

  if player_choice in items:
    cpu_choice = random.choice(items)
    print(f"Player ({player_choice}): CPU ({cpu_choice})")

    if player_choice == cpu_choice:
      print("Its a tie, try again.")
    else:
      #do checks
      if player_choice == "R" and cpu_choice == "S":
        print("Rock smash Scissors. Player Wins!")
     
      elif player_choice == "P" and cpu_choice == "R":
        print("Paper smash Rock. Player Wins!")
        
      elif player_choice == "S" and cpu_choice == "P":
        print("Scissors smash Paper. Player Wins!")
    
      elif player_choice == "S" and cpu_choice == "R":
        print("Rock smash Scissors. CPU Wins")
        
      elif player_choice == "R" and cpu_choice == "P":
        print("Paper smash Rock. CPU Wins!")
        
      else:
        print("Scissors smash Paper. CPU Wins!")
        
      #Extra: To ask the user if they want to continue or not
      play_again = input("Play again? (y/n): ").lower()

      if play_again != "y" or play_again == "n" or play_again == "n":
        break
      
  else:
    print("Error! Please enter a valid choice")
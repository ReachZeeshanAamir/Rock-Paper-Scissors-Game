import random

user_wins = 0
computer_wins = 0

options = ("rock","paper","scissors")

while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()
    if user_input == "q":
        break
    
    
    if user_input not in options:
        print("Enter a valid option")
        continue

    random_number =  random.randint(0,2)
    computer_choice = options[random_number]
    print("Computer picked", computer_choice + ".")
    if user_input== "rock" and computer_choice== "scissors":
        print("You win!")
        user_wins += 1 
    elif user_input== "paper" and computer_choice== "rock":
        print("You win!")
        user_wins += 1 
    elif user_input== "scissors" and computer_choice== "paper":
        print("You win!")
        user_wins += 1 
    elif user_input == computer_choice:
        print("Its a tie")
    else:
        print("You Lost")
        computer_wins +=1 
print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")
print("GoodBye! 🥲")
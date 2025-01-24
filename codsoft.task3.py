import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    
    return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors")
    
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        
        user_choice = input("Enter your choice(rock, paper, or scissors):").lower()
        
        if user_choice not in choices:
            print("Invalid choice")
            continue
        
        
        computer_choice = random.choice(choices)
        print(f"\nYou choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        
        play_again = input("\nDo you want to play again(yes/no):").lower()
        if play_again!='yes':
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    play_game()

import random
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
def determine_winner(user_choice, computer_choice):
    if(user_choice == computer_choice):
        return "It's a tie!"
    elif(user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"\nScores -> You: {user_score}, Computer: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break
play_game()

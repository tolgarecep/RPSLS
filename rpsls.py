# Human vs. Computer in "Rock, Paper, Scissors, Lizard, Spock"
#
# Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons spock, spock smashes scissors,
# scissors decapitates lizard, lizard eats paper, paper disproves spock, spock vaporizes rock, rock crushes scissors.

while True:
  human_move = input("Your move: ")

  move_list = ["rock", "paper", "scissors", "lizard", "spock"]
  import random
  computer_move = random.choice(move_list)

  # deduplicated draw possibilities
  if human_move == computer_move:
    print("Computer's move: " + random.choice(move_list))
    print("Draw!")

  # scissors & paper
  if human_move == "scissors" and computer_move == "paper":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "paper" and computer_move == "scissors":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # paper & rock
  if human_move == "paper" and computer_move == "rock":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "rock" and computer_move == "paper":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # rock & lizard
  if human_move == "rock" and computer_move == "lizard":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "lizard" and computer_move == "rock":
    print("Computer's move: " + random.choice(move_list))
    print("Computer win!")

  # lizard & spock
  if human_move == "lizard" and computer_move == "spock":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "spock" and computer_move == "lizard":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # spock & scissors
  if human_move == "spock" and computer_move == "scissors":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "scissors" and computer_move == "spock":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # scissors & lizard
  if human_move == "scissors" and computer_move == "lizard":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "lizard" and computer_move == "scissors":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # lizard & paper
  if human_move == "lizard" and computer_move == "paper":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "paper" and computer_move == "lizard":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # paper & spock
  if human_move == "paper" and computer_move == "spock":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "spock" and computer_move == "paper":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # spock & rock
  if human_move == "spock" and computer_move == "rock":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "rock" and computer_move == "spock":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")

  # rock & scissors
  if human_move == "rock" and computer_move == "scissors":
    print("Computer's move: " + random.choice(move_list))
    print("You won!")
  if human_move == "scissors" and computer_move == "rock":
    print("Computer's move: " + random.choice(move_list))
    print("Computer wins!")
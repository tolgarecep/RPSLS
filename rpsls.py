# Human vs. Computer in "Rock, Paper, Scissors, Lizard, Spock"
#
# Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons spock, spock smashes scissors,
# scissors decapitates lizard, lizard eats paper, paper disproves spock, spock vaporizes rock, rock crushes scissors.

while True:
  human_move = input("Choose wisely: ")

  move_list = ["rock", "paper", "scissors", "lizard", "spock"]
  import random
  computer_move = random.choice(move_list)

  # draw
  if human_move == computer_move:
    print("Draw!")

  # scissors & paper
  if human_move == "scissors" and computer_move == "paper":
    print("You won against paper!")
  if human_move == "paper" and computer_move == "scissors":
    print("Computer wins with scissors!")

  # paper & rock
  if human_move == "paper" and computer_move == "rock":
    print("You won against rock!")
  if human_move == "rock" and computer_move == "paper":
    print("Computer wins with paper!")

  # rock & lizard
  if human_move == "rock" and computer_move == "lizard":
    print("You won against lizard!")
  if human_move == "lizard" and computer_move == "rock":
    print("Computer wins with rock!")

  # lizard & spock
  if human_move == "lizard" and computer_move == "spock":
    print("You won against spock!")
  if human_move == "spock" and computer_move == "lizard":
    print("Computer wins with lizard!")

  # spock & scissors
  if human_move == "spock" and computer_move == "scissors":
    print("You won against scissors!")
  if human_move == "scissors" and computer_move == "spock":
    print("Computer wins with spock!")

  # scissors & lizard
  if human_move == "scissors" and computer_move == "lizard":
    print("You won against lizard!")
  if human_move == "lizard" and computer_move == "scissors":
    print("Computer wins with scissors!")

  # lizard & paper
  if human_move == "lizard" and computer_move == "paper":
    print("You won against paper!")
  if human_move == "paper" and computer_move == "lizard":
    print("Computer wins with lizard!")

  # paper & spock
  if human_move == "paper" and computer_move == "spock":
    print("You won against spock!")
  if human_move == "spock" and computer_move == "paper":
    print("Computer wins with paper!")

  # spock & rock
  if human_move == "spock" and computer_move == "rock":
    print("You won against rock!")
  if human_move == "rock" and computer_move == "spock":
    print("Computer wins with spock!")

  # rock & scissors
  if human_move == "rock" and computer_move == "scissors":
    print("You won against scissors!")
  if human_move == "scissors" and computer_move == "rock":
    print("Computer wins with rock!")
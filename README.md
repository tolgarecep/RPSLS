# RPSLS

A game of chance (!) which you can play with your computer.

## Rules

When executed, your computer will ask you to pick a move among rock, paper, scissors, lizard and spock and then it will pick one and your moves will be compared and conclusion
will get determined based on this dominance relations: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons spock, spock smashes scissors, scissors
decapitates lizard, lizard eats paper, paper disproves spock, spock vaporizes rock, rock crushes scissors.

## Misc.

The first large-scale study about people playing rock-paper-scissors reveal a way to beat the game. Researchers found that people made random decisions only 1/3 of the time
they played rock-paper-scissors (RPS), and the rest of the time they changed their preferences based on their winning and losing status in the previous game. In other words, in
the RPS game, the winner of the game repeats the previous winning behavior more often, while the losers prefer the move that will beat the previous one. This is not the case when
you play with computer programmed to pick one of the moves randomly but given that we know so little about randomness, it worths a try.

Also thinking about few arbitrary changes such as cumulatively working score table (working per execution) and a little different way for computer to behave after you pick your
move.
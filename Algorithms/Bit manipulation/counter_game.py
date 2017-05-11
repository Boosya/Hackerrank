# Counter game solution

# Louise and Richard play a game. They have a counter set to N. Louise gets the first turn and the turns alternate thereafter. In the game, they perform the following operations.
#
# If N is not a power of 2, reduce the counter by the largest power of 2 less than N.
# If N is a power of , reduce the counter by half of N.
# The resultant value is the new N which is again used for subsequent operations.
# The game ends when the counter reduces to 1, i.e., N == 1, and the last person to make a valid move wins.
#
# Given , your task is to find the winner of the game.

# written by Ekaterina Boosya Gasparian

# checks of n is power of 2
def is_power_of_2(n):
    return (n&(n-1) == 0)

# reduces n by  largest power of 2 less than n
def reduce_ny_next_power_2(n):
    # calculate where is the first 1 in bit representaion of the n
    nb_bits = 1
    while n >> nb_bits != 0:
        nb_bits += 1
    # create mask of form 01..1 to remove first 1 from n
    mask = 1 << nb_bits-1
    mask  = mask - 1
    return n & mask

def game(n):
	count = 0 # keeps track of number of moves
	while n!= 1:
		if is_power_of_2(n):
			n = n >> 1
		else:
			n = reduce_ny_next_power_2(n)
		count += 1
    # check who wins based on number of moves
	if count%2 == 0:
		return("Richard")
	else:
		return("Louise")


if __name__ == "__main__":
    nb_games = int(input())
    for _ in range(nb_games):
        n = int(input())
        print(game(n))

"""
This Python code simulates a two-player math game where players take turns removing perfect squares from a pile of
 numbers.
The game starts by prompting the user to enter a non-square number between 10 and 1000. Perfect squares are integers
 which can be obtained by squaring an integer (e.g., 4 is a perfect square because 2 * 2 = 4). Once a valid number is
  entered, the game begins.

On each turn, a player is prompted to enter a valid perfect square to remove from the pile. Valid perfect squares are
 1, 4, 9, 16, and so on. The player cannot enter a number greater than the remaining number of squares in the pile.
  After a valid square is entered, it is subtracted from the pile.

The game continues until the pile reaches zero. The player who removes the last perfect square wins the game!
"""

# File: Subtract a square in python.
# Author: Yousef Hesham Ali Ali Zayan

#starting game and checking if inputed number is square number or not
def gamee():
    while True:
        nu1 = int(input("Enter a non-square number between 10 and 1000: "))
        if 10 <= nu1 <= 1000 and not isperfect(nu1):
            return nu1
        print("Invalid number, Please enter a non square number between 10 and 1000")
def isperfect(nu2):
    if nu2 < 0:
        return False

    root = int(nu2**0.5)
    return root * root == nu2

def subtract_squ():
    nu = gamee()
    pile = nu
    player = 1 #starting with player 1

# making the user know the number of remaining piles after subtracting the previous entered square numbers from both users
    while pile > 0:
        print(f"Number of remaining piles: {pile}")
        squ = -1
        # checking if the entered user's number is valid or not
        while squ <= 0 or squ not in [1, 4, 9, 16, *[i ** 2 for i in range(2, int(pile ** 0.5) + 1)]]:
            try:
                squ = int(input(f"Player {player}'s turn, enter a valid square number (1, 4, 9, 16, ...): "))
                # Checks if the entered number is bigger than the remained number of piles or not
                while squ > pile:
                    max_squ = int(pile ** 0.5) ** 2
                    print(f"Please enter a square number smaller than or equal to {max_squ}")
                    squ = int(input(f"Player {player}'s turn, enter a valid square number (1, 4, 9, 16, ...): "))

            except ValueError:
                print("Invalid input, Enter a valid number.")


        pile -= squ
        # Announce the winner after subtracting the last pile
        if pile == 0:
            print(f"Player {player} wins!")
            return

        player = 2 if player == 1 else 1  # Switch players

subtract_squ()
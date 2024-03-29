
# Tic-Tac-Toe with Min-Max AI
This is a simple Python program that allows you to play Tic-Tac-Toe against a Min-Max AI.

### Installation
To run the program, you'll need to have Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, download the tic_tac_toe.py file and save it to a directory of your choice.

### How to Play
To play the game, open up your terminal or command prompt and navigate to the directory where you saved the tic_tac_toe.py file. Then, enter the following command:

'''
python tic_tac_toe.py 
'''
This will start the game. The board will be displayed in the terminal, and you will be prompted to make a move by entering the row and column of the cell where you want to place your piece. For example, to place your piece in the top-left corner, you would enter "1 1".

The Min-Max AI will automatically make its move after you make yours. The game will continue until someone wins or the board is full.

### How the Min-Max AI Works
The Min-Max AI uses the min-max algorithm to determine the best move to make. Essentially, it considers all possible moves that it and its opponent can make and assigns a score to each one based on how likely it is to lead to a win. It then chooses the move with the highest score.

The min-max algorithm is a recursive algorithm that explores all possible moves to a certain depth. In this program, the depth is set to 5, which means that the algorithm will consider all possible moves 5 turns ahead. This makes the AI quite difficult to beat!

### Future Improvements
Here are some ideas for how the program could be improved in the future:

Add a graphical interface to make it easier to see the board and make moves.
- Implement alpha-beta pruning to make the min-max algorithm more efficient.
- Add an option to choose the depth of the min-max algorithm, so players can adjust the difficulty.
- Add an option to play against another human player.

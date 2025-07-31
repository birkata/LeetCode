"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

 - Players take turns placing characters into empty squares ' '.
 - The first player A always places 'X' characters, while the second player B always places 'O' characters.
 - 'X' and 'O' characters are always placed into empty squares, never on filled ones.
 - The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
 - The game also ends if all squares are non-empty.
 - No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on
grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw".
If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will
 play first.

 Constraints:

- 1 <= moves.length <= 9
- moves[i].length == 2
- 0 <= rowi, coli <= 2
- There are no repeated elements on moves.
- moves follow the rules of tic tac toe.

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

"""

from typing import List
from itertools import combinations


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        moves_lst = [','.join(map(str, el)) for el in moves]

        winning_positions = [{'0,0', '0,1', '0,2'},
                             {'1,0', '1,1', '1,2'},
                             {'2,0', '2,1', '2,2'},
                             {'0,0', '1,0', '2,0'},
                             {'0,1', '1,1', '2,1'},
                             {'0,2', '1,2', '2,2'},
                             {'0,0', '1,1', '2,2'},
                             {'2,0', '1,1', '0,2'}]

        moves_a = [p for i, p in enumerate(moves_lst) if i % 2 == 0]
        moves_b = [p for i, p in enumerate(moves_lst) if i % 2 != 0]

        def arbiter(lst: List[str]) -> bool:
            for combination in combinations(lst, 3):
                if set(combination) in winning_positions:
                    return True
            return False

        if arbiter(moves_a):
            return ('A')
        elif arbiter(moves_b):
            return ('B')
        elif len(moves) == 9:
            return ('Draw')
        else:
            return ('Pending')

if __name__ == "__main__":
    sol_instance = Solution()
    print(sol_instance.tictactoe(moves=[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))

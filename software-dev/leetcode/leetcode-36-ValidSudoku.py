from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.verifyList(row):
                return False

        transposedBoard = [[board[i][o] for i in range(9)] for o in range(9)]


        for row in transposedBoard:
            if not self.verifyList(row):
                return False

        for row in range(1,4):
            for col in range(1,4):
                square = [board[i][o] for i in range(3*row-3, 3*row) for o in range(3*col-3, 3*col)]
                if not self.verifyList(square):
                    return False
        return True


    def verifyList(self, list: List[str]):
        storage = set()
        for element in list:
            if element != '.':
                if element in storage:
                    return False
                else:
                    storage.add(element)
        return True

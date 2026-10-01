class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def count(arr):
            dick = Counter(x for x in arr if x != '.')
            valid = True
            for d in dick.values():
                if d != 1:
                    valid = False
                    break
            return valid

        row, col = len(board), len(board[0])
        # 1st rule:
        for r in board:
            if not count(r):
                return False
        # 2st rule:
        for c in range(col):
            arr = []
            for r in range(row):
                arr.append(board[r][c])
            if not count(arr):
                return False
        # 3rd rule:
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in squares[(r//3,c//3)]:
                    return False
                squares[(r//3, c//3)].add(board[r][c])
        return True
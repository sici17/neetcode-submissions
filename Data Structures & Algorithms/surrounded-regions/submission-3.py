class Solution:
    def solve(self, board: List[List[str]]) -> None:

        q = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(board)):
            if board[i][0] == "O":
                board[i][0] = "S"
                q.append((i, 0))
            if board[i][len(board[0]) - 1] == "O":
                board[i][len(board[0]) - 1] = "S"
                q.append((i, len(board[0]) - 1))

        for j in range(1, len(board[0]) - 1):
            if board[0][j] == "O":
                board[0][j] = "S"
                q.append((0, j))
            if board[len(board) - 1][j] == "O":
                board[len(board) - 1][j] = "S"
                q.append((len(board) - 1, j))

        while q:
            i, j = q.popleft()

            for dr, dc in directions:
                row = i + dr
                col = j + dc

                if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O":
                    board[row][col] = "S"
                    q.append((row, col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"










        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        edge = set()
        for c in range(cols):
            edge.add((0, c))
            edge.add((rows-1, c))
        for r in range(rows):
            edge.add((r, 0))
            edge.add((r, cols-1))


        def bfs(r, c):
            q = collections.deque()
            q.append([r, c])
            board[r][c] = "S"

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if(nr < 0 or nc < 0 or nr == rows or nc == cols or board[nr][nc] != "O"):
                        continue
                    board[nr][nc] = "S"
                    q.append([nr, nc])

                    


        for r, c in edge:
            if board[r][c] == "O":
                bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
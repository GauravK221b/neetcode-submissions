class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        inf = 2147483647

        def bfs(r, c):
            q = collections.deque()
            q.append([r, c])
            seen = {(r, c)}
            steps = 0

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if(nr < 0 or nc < 0 or nr >= rows or
                            nc >= cols or (nr, nc) in seen or grid[nr][nc] == -1):
                            continue
                        
                        seen.add((nr, nc))
                        q.append((nr, nc))
                steps += 1
            return inf




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == inf:
                    grid[r][c] = bfs(r, c)


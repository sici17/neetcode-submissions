class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        def verifica(row, col, i, j, visited):
            if (
                0 <= row < rows
                and 0 <= col < cols
                and (row, col) not in visited
                and heights[row][col] >= heights[i][j]
            ):
                return True
            return False

        rows = len(heights)
        cols = len(heights[0])

        qp = deque()
        qa = deque()

        seta = set()
        setp = set()

        for j in range(cols):
            qp.append((0, j))
            qa.append((rows - 1, j))
            setp.add((0, j))
            seta.add((rows - 1, j))

        for i in range(rows):
            qp.append((i, 0))
            qa.append((i, cols - 1))
            setp.add((i, 0))
            seta.add((i, cols - 1))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while qa or qp:
            for _ in range(len(qa)):
                r, c = qa.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if verifica(row, col, r, c, seta):
                        qa.append((row, col))
                        seta.add((row, col))

            for _ in range(len(qp)):
                r, c = qp.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if verifica(row, col, r, c, setp):
                        qp.append((row, col))
                        setp.add((row, col))

        return [[r, c] for r, c in (seta & setp)]


        

        






        
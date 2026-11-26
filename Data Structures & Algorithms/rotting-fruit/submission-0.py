class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh=0
        time=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1: 
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while fresh>0 and q:
            for i in range(len(q)):
                i,j=q.popleft()

                for dr,dc in directions:
                    row=i+dr
                    col=j+dc

                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1:
                        grid[row][col]=2
                        q.append((row,col))
                        fresh-=1

            time+=1
        
        return time if fresh==0 else -1




                







        

        
        
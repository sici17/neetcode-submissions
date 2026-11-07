class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        path=[]

        visitati=set()

        def ammesso(nodo):
            r,c=nodo
            return board[r][c]==word[len(path)]
        
        def vicini(nodo):
            r, c = nodo
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc<len(board[0]):
                    yield nr, nc


        def dfs(nodo):

            if nodo in visitati or not ammesso(nodo):
                return
            
            path.append(nodo)
            visitati.add(nodo)

            trovato=len(path)==len(word)

            if not trovato:
                for prossimo in vicini(nodo):
                    if dfs(prossimo):
                        trovato=True
                        break
            
            visitati.remove(nodo)
            path.pop()
            return trovato
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs((r, c)):  
                    return True

        return False


            












        
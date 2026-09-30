class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        righe=0
        colonne=0
        maxcolonne=len(matrix[0])-1
        maxrighe=len(matrix)-1

        while colonne<=maxcolonne and righe<=maxrighe:

            rigamid=(maxrighe+righe)//2
            colonnamid=(maxcolonne+colonne)//2

            val=matrix[rigamid][colonnamid]

            if(target==val):
                return True
            
            elif(target>val):
                if target>matrix[rigamid][maxcolonne]:
                    righe=rigamid+1
                else:
                    colonne=colonnamid+1                
            
            else:
                if target<matrix[rigamid][0]:
                    maxrighe=rigamid-1
                else:
                    maxcolonne=colonnamid-1


        return False

        
        
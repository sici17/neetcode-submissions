class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res=[]
        path=[]

        if len(digits)==0:
            return []

        lettere = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz",
        }

        def dfs(i):

            if i==len(digits):
                res.append("".join(path))
                return

            for lettera in lettere[digits[i]]:
                path.append(lettera)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return res
            





        
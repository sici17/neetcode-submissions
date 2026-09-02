class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first= strs[0]
        prefix=0

        for i in range(len(first)):

            for word in strs[1:]:

                if(not (i<len(word)) or first[i]!= word[i]):
                    print(first[i])
                    return first[:prefix]

            prefix+=1
                
        return first         






        


        
        





class Solution:
    def reorganizeString(self, s: str) -> str:

        mappa={}
        ret=[]

        for char in s:
            mappa[char]=mappa.get(char,0)+1
        
        heap = [(-val, key) for key, val in mappa.items()]
        heapq.heapify(heap) 
        if abs(heap[0][0])>(len(s)+1)/2:
            return ""
        print(heap)
        

        while heap:
            count1, char1=heapq.heappop(heap)
            ret.append(char1)
            if heap:
                count2, char2=heapq.heappop(heap)
                ret.append(char2)
            if count1+1<0:
                heapq.heappush(heap,(count1+1,char1))
            if count2+1<0:
                heapq.heappush(heap,(count2+1,char2))
        
        return "".join(ret)






        
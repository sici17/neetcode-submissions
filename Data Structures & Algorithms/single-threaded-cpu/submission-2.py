class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        time=0
        dati=[]
        heap=[]
        heapq.heapify(heap)
        ret=[]

        for i in range(len(tasks)):
            dati.append((tasks[i][0],tasks[i][1],i))
        
        dati=deque(sorted(dati, key=lambda x: x[0]))

        while dati or heap:

            if not heap and time < dati[0][0]:
                time = dati[0][0]
            
            while dati and dati[0][0] <= time:
                enq, proc, idx = dati.popleft()
                heapq.heappush(heap, (proc, idx))
            
            proc, idx = heapq.heappop(heap)
            time += proc
            ret.append(idx)
        
        return ret

            

        

        

        

        

        

        



        

        






        
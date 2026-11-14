class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        mappa=Counter(tasks)
        frequenza=[-s for s in mappa.values()]
        heapq.heapify(frequenza)
        q=deque()
        time=0

        while frequenza or q:
            time+=1
            if not frequenza:
                time=q[0][1]           
            else:
                cnt=1+heapq.heappop(frequenza)

                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1]==time:
                heapq.heappush(frequenza,q.popleft()[0])
        
        return time







        



        

        





        







        


        
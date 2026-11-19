class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda t: t[1])
        heap=[]
        heapq.heapify(heap)
        carico=0

        for trip in trips:
            if heap:
                while heap:
                    if heap[0][0]<= trip[1]:
                        carico-=heap[0][1]
                        heapq.heappop(heap)
                    else:
                        break

            heapq.heappush(heap,(trip[2],trip[0]))
            carico+=trip[0]
            if carico>capacity:
                return False
        
        return True


            
        
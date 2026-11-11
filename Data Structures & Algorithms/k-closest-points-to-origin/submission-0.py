class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distanze=[]
        visti=set()

        for point in points:
            tupla=(point[0],point[1])
            if tupla in visti:
                continue
            distanze.append((-math.sqrt(point[0]**2+point[1]**2),point))
            visti.add(tupla)
        
        heapq.heapify(distanze)

        while len(distanze)>k:
            heapq.heappop(distanze)
        
        for i in range(len(distanze)):
            distanze[i]=distanze[i][1]
        return distanze
        







        
        
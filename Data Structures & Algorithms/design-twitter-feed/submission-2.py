class Twitter:

    def __init__(self):
        self.heap=[]
        heapq.heapify(self.heap)
        self.mappa=defaultdict(set)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time+=1

        heapq.heappush(self.heap,(-self.time,(tweetId,userId)))

        

    def getNewsFeed(self, userId: int) -> List[int]:

        count=0
        heap_copy = self.heap.copy()
        ret=[]

        while heap_copy and count<10:

            tweet=heapq.heappop(heap_copy)
            
            if  tweet[1][1] in self.mappa[userId] or tweet[1][1] == userId:
                ret.append(tweet[1][0])
                count+=1
        
        return ret


        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.mappa[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.mappa[followerId].discard(followeeId)
        

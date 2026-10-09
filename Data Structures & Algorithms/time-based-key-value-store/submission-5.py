class TimeMap:

    def __init__(self):

        self.mappa=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.mappa[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        l=0
        r=len(self.mappa[key])-1
        ret=""

        while l<=r:

            mid= (l+r)//2

            if self.mappa[key][mid][0]<=timestamp:
                ret=self.mappa[key][mid][1]
                l=mid+1
            else:
                r=mid-1
        
        return ret





        

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = {}
        self.followmap = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetmap:
            self.tweetmap[userId] = []
        
        self.tweetmap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minheap = []


        # self.followmap[userId] = self.followmap[userId].add(userId)
        # self.followmap[userId] = set([userId])
        if userId not in self.followmap:
            self.followmap[userId] = set()
            
        self.followmap[userId].add(userId)
        for followeeID in self.followmap[userId]:
            if followeeID in self.tweetmap:
                index = len(self.tweetmap[followeeID]) - 1
                time, tweetId = self.tweetmap[followeeID][-1]
                minheap.append((time, tweetId, followeeID, index - 1))
        
        heapq.heapify(minheap)
        while minheap and len(result)<10:
            time, tweetId, followeeID, next_index = heapq.heappop(minheap)

            result.append(tweetId)

            if next_index >= 0:
                time, tweetId = self.tweetmap[followeeID][next_index]
                heapq.heappush(minheap, (time, tweetId, followeeID, next_index - 1))
            
        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap:
            self.followmap[followerId].discard(followeeId)
        

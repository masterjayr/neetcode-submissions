class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userid -> tweetIds
        self.followMap = defaultdict(set) # userid -> followeeIds meaning people userId is following

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        self.followMap[userId].add(userId)
        # for every person userId follows
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: # if person has a tweet
                index = len(self.tweetMap[followeeId]) - 1 # get last index of tweet for that person
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10: 
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) # me to follow someone - so add to my list(set) the person(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: # if i'm currently following followeeId check
            self.followMap[followerId].remove(followeeId)

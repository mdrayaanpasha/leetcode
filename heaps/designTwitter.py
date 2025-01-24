import heapq

class Twitter:

    def __init__(self):
        self.users = {}
        self.count = 0

    def postTweet(self, userId, tweetId):
        if userId not in self.users:
            self.users[userId] = {'posts': [], 'following': set()}
        
        self.count+=1
        self.users[userId]['posts'].append((self.count,tweetId))

        

    def follow(self, followerId, followeeId):
        if followerId not in self.users:
            self.users[followerId] = {'posts': [], 'following': set()}

        if followeeId not in self.users:
            self.users[followeeId] = {'posts': [], 'following': set()}

        self.users[followerId]['following'].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.users and followeeId in self.users[followerId]['following']:
            self.users[followerId]['following'].remove(followeeId)

    
    def getNewsFeed(self, userId):

        if userId not in self.users:
            return []

        heap = []

        for timestamp,tweetId in self.users[userId]['posts']:
            heapq.heappush(heap,(timestamp,tweetId))
            if len(heap) > 10:
                heapq.heappop(heap)
            
        for followeeId in self.users[userId]['following']:
            for timestamp,tweetId in self.users[followeeId]['posts']:
                heapq.heappush(heap,(timestamp,tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)

        return [tweetId for _,tweetId in sorted(heap,reverse=True)]
      


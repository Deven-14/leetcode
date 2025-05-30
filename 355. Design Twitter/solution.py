from collections import defaultdict, deque
import heapq
class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(lambda: deque(maxlen=10))
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        if len(self.tweets[userId]):
            timestamp, tweetId = self.tweets[userId][0]
            heap.append((-timestamp, tweetId, userId, 1))
        
        for followeeId in self.followers[userId]:
            if len(self.tweets[followeeId]):
                timestamp, tweetId = self.tweets[followeeId][0]
                heap.append((-timestamp, tweetId, followeeId, 1))
            
        heapq.heapify(heap)

        feeds = []
        while heap and len(feeds) < 10:
            (timestamp, tweetId, personId, next_idx) = heapq.heappop(heap)
            feeds.append(tweetId)
            if next_idx < len(self.tweets[personId]):
                timestamp, tweetId = self.tweets[personId][next_idx]
                heapq.heappush(heap, (-timestamp, tweetId, personId, next_idx + 1))
        
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
import heapq
class Twitter:

    def __init__(self):
        self.user_follow_map = {}
        self.tweets = {}
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_follow_map:
            self.user_follow_map[userId] = set()
            self.user_follow_map[userId].add(userId)
            
        if userId not in self.tweets:
            self.tweets[userId] = []
            
        self.tweets[userId].append([self.clock, tweetId])
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_follow_map:
            return []
        
        heap = []
        topTenTweetIds = []
        currTweetMap = {}
        for followee in self.user_follow_map[userId]:
            if followee in self.tweets:
                no_of_tweets = len(self.tweets[followee])
                currTweetMap[followee] = no_of_tweets-1
                if no_of_tweets > 0:
                    heapq.heappush(heap, [-self.tweets[followee][no_of_tweets-1][0], self.tweets[followee][no_of_tweets-1][1], followee])
                
        while heap and len(topTenTweetIds) < 10:
            curr = heapq.heappop(heap)
            topTenTweetIds.append(curr[1])
            curr_tweet = currTweetMap[curr[2]]
            curr_tweet -= 1
            currTweetMap[curr[2]] = curr_tweet
            if curr_tweet >= 0:
                heapq.heappush(heap, [-self.tweets[curr[2]][curr_tweet][0], self.tweets[curr[2]][curr_tweet][1], curr[2]])
                    
        return topTenTweetIds
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follow_map:
            self.user_follow_map[followerId] = set()
            self.user_follow_map[followerId].add(followerId)
        self.user_follow_map[followerId].add(followeeId)
        return 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followerId in self.user_follow_map and followeeId in self.user_follow_map[followerId]:
            self.user_follow_map[followerId].remove(followeeId)
        return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
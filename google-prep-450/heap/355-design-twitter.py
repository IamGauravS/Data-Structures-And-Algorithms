import heapq
from typing import List, Dict, Set, Tuple

class Twitter:
    def __init__(self):
        # Dictionary to store user tweets as lists of tuples (time, tweetId)
        self.userTweet: Dict[int, List[Tuple[int, int]]] = {}
        # Dictionary to store followed users for each user as sets
        self.followedByUser: Dict[int, Set[int]] = {}
        # A counter to maintain the timestamp for each tweet
        self.time = 0

    def ensureUser(self, userId: int):
        # Initializes the user's tweet list and follow set if they don't exist
        if userId not in self.userTweet:
            self.userTweet[userId] = []
        if userId not in self.followedByUser:
            self.followedByUser[userId] = {userId}  # User follows themselves by default

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ensureUser(userId)
        # Add the tweet with a negative timestamp for max-heap behavior
        self.userTweet[userId].append((-self.time, tweetId))
        self.time += 1  # Increment the timestamp for each new tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get the most recent 10 tweets from the user's feed
        recent10Tweets = []
        feedHeap = []
        
        # Gather the latest tweet from each followed user
        for user in self.followedByUser.get(userId, []):
            if self.userTweet[user]:
                # Push the most recent tweet of each user into the heap
                index = len(self.userTweet[user]) - 1
                time, tweetId = self.userTweet[user][index]
                heapq.heappush(feedHeap, (time, tweetId, user, index - 1))

        # Extract up to 10 most recent tweets
        while feedHeap and len(recent10Tweets) < 10:
            time, tweetId, user, index = heapq.heappop(feedHeap)
            recent10Tweets.append(tweetId)
            # If there are more tweets for the user, push the next one into the heap
            if index >= 0:
                nextTime, nextTweetId = self.userTweet[user][index]
                heapq.heappush(feedHeap, (nextTime, nextTweetId, user, index - 1))

        return recent10Tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.ensureUser(followerId)
        # Add the followee to the follower's follow set
        self.followedByUser[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followee from the follower's follow set if it exists and is not the follower themselves
        if followerId in self.followedByUser and followeeId != followerId:
            self.followedByUser[followerId].discard(followeeId)

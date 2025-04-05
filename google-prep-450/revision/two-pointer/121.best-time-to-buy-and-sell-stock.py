#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

import https
import math

logs = {
    "events" : [
        {"id": 1, "timestamp" : "32323", "message": "ffsjfksnfks"},
        {"id": 1, "timestamp" : "32323", "message": "ffsjfksnfks"}

    ]
}

api = https://get-logs.com/{startTime}&{endTime}

class Solution:

    def __init__(self):
        self.bust_list = []

    def get_logs_data(startTime, endTime):
        # hit the api
        response = https.get(https://get-logs.com/{startTime}&{endTime})
        result_data = response.json()
        total_logs = (result_data['events'])
        if total_logs >= 1000 + endTime- startTime:
            return True
        return False

    def getBurstsUtil(self, startTIme, endTIme):

        if endTIme> startTIme:
            has_busrst = self.get_logs_data(startTIme, endTIme)
            
            if has_busrst:
                if endTIme - startTIme == 1:
                    self.bust_list.append(startTIme)

                else:
                    self.getBursts(startTIme, math.ceil(endTIme/2))
                    self.getBursts(math.ceil(endTIme/2)+1 , endTIme/2)

    def getBurst(self, startTime, endTime):
        self.getBurstsUtil(startTime, endTime)

        return self.bust_list

        
        
        

        
        
# @lc code=end


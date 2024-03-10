class RequestLogger:
    def __init__(self, time_limit):
        # Initialize your data structure here
        self.request_dict = {}
        self.time_limit = time_limit

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp, request):
        # Replace this placeholder return statement with your code
        curr_timestamp = timestamp
        request = request
        
        if request not in self.request_dict:
            self.request_dict[request] = curr_timestamp
            return True 
        else:
            previous_time = self.request_dict[request]
            if curr_timestamp - previous_time >= self.time_limit:
                self.request_dict[request] = curr_timestamp
                return True  
            else:
                return False

class TimeStamp:
    def __init__(self):
        self.values_dict = {}
        self.timestamps_dict = {}

    #  Set TimeStamp data variables
    def set_value(self, key, value, timestamp):

        # Write your code here
        if key not in self.values_dict:
            self.values_dict[key] = []
            
        self.values_dict[key].append(value)
        if key not in self.timestamps_dict:
            self.timestamps_dict[key] = []
            
        self.timestamps_dict[key].append(timestamp)

    # Get TimeStamp data variables
    def get_value(self, key, timestamp):

        # Write your code here
        if key not in self.timestamps_dict:
            return ""
        
        if timestamp > self.timestamps_dict[key][-1]:
            return self.values_dict[key][-1]
        
        else:
            if timestamp in self.timestamps_dict[key]:
                return self.values_dict[key][self.timestamps_dict[key].index(timestamp)]  ## we can use binary search here
            else:
                return ""

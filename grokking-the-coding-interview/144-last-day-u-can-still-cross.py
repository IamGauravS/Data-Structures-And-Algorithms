class SnapshotArray:
    # Constructor
    def __init__(self, length):
        # Write your code here
        self.array = [0]*length
        self.snapshot_dic = {}
        self.snapshot_id = 0

    # Function set_value sets the value at a given index idx to val. 
    def set_value(self, idx, val):
        # Write your code here
        self.array[idx-1] = val
        
    
    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1. 
    def snapshot(self):
        # Replace this placeholder return statement with your code
        self.snapshot_dic[self.snapshot_id] = self.array.copy()
        self.snapshot_id +=1 
        return self.snapshot_id-1
    
    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snapid):
        # Replace this placeholder return statement with your code
        return self.snapshot_dic[snapid][idx-1]

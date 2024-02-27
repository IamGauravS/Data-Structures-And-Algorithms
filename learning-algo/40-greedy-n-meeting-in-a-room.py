"""
This function is used to find the maximum number of meetings that can be attended, given the start and end times of the meetings.

The logic behind the function is as follows:
1. We first create a list of tuples, where each tuple represents a meeting and contains its start time, end time, and index.
2. We then sort this list of meetings by their end times. The reason for this is that to maximize the number of meetings, we should always pick the meeting that ends the earliest.
3. We initialize the end time of the last attended meeting to 0 and create an empty list to store the indices of the attended meetings.
4. We then iterate over the sorted list of meetings. For each meeting, if its start time is not earlier than the end time of the last attended meeting, we attend the meeting and update the end time and the list of attended meeting indices.
5. Finally, we return the list of attended meeting indices.

Parameters:
start (list): A list of integers representing the start times of the meetings.
end (list): A list of integers representing the end times of the meetings.

Returns:
list: A list of integers representing the indices of the attended meetings.
"""

def find_num_of_max_meetings(start, end):
    # Create a list of tuples where each tuple contains the start time, end time, and index of a meeting
    meetings = [(start[i], end[i], i) for i in range(len(start))]

    # Sort the meetings by end time
    sorted_meetings = sorted(meetings, key=lambda x: x[1])

    # Initialize the end time of the last attended meeting and the list of attended meeting indices
    endtime = 0
    index_output = []

    # Iterate over the sorted meetings
    for meeting in sorted_meetings:
        # If the start time of the current meeting is not earlier than the end time of the last attended meeting, attend the meeting
        if meeting[0] >= endtime:
            endtime = meeting[1]
            index_output.append(meeting[2])

    # Return the list of attended meeting indices
    return index_output




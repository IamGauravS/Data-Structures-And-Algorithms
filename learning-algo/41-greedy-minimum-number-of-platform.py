def find_maximum_no_platform_occupied_together(arrival, departure):
    # Sort the arrival and departure times
    arrival.sort()
    departure.sort()

    # Initialize pointers for arrival and departure times
    start_pointer = 0
    departure_pointer = 0

    # Initialize the maximum number of occupied platforms and the current number of occupied platforms
    max_no_of_occupied_platform = 0
    occupied_platforms = 0

    # Iterate while there are trains to arrive
    while start_pointer < len(arrival):
        # If the next train arrives before the next train departs, increment the number of occupied platforms
        if arrival[start_pointer] <= departure[departure_pointer]:
            occupied_platforms += 1
            start_pointer += 1
        # If the next train departs before the next train arrives, decrement the number of occupied platforms and increment the departure pointer
            ## here we dont go to next start pointer untill we have cleared all the trains which have already departed
            ## this will give us the correct situation at that time
        else:
            occupied_platforms -= 1
            departure_pointer += 1

        # Update the maximum number of occupied platforms
        if occupied_platforms > max_no_of_occupied_platform:
            max_no_of_occupied_platform = occupied_platforms

    return max_no_of_occupied_platform
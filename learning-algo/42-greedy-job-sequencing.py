def find_maximum_profit(jobs):
    # Sort the jobs by their index in descending order
    # This ensures that jobs with higher index (and potentially higher profit) are considered first
    jobs_sorted_by_profit = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Find the maximum deadline among all jobs
    # This will be used to initialize the slots for jobs
    max_no_of_days = max(job[1] for job in jobs)

    # Initialize the slots for jobs with -1
    # Each slot represents a day, and the value in the slot represents the index of the job scheduled on that day
    # Initially, all slots are empty, represented by -1
    slots = [-1]*max_no_of_days

    # Initialize the total profit to 0
    profit = 0

    # Iterate over the jobs, starting from the job with the highest index
    for job in jobs_sorted_by_profit:
        # Get the deadline for this job
        deadline = job[1]

        # Try to find a slot for this job
        # Start from the slot corresponding to the deadline and go backwards
        # If the slot is already occupied (i.e., not equal to -1), move to the previous slot
        while slots[deadline-1] != -1 and deadline > 0:
            deadline -= 1

        # If a free slot is found and the deadline has not passed, assign this job to that slot
        if deadline > 0:
            slots[deadline-1] = job[2]

            # Add the profit of this job to the total profit
            profit += job[0]

    # Return the total profit
    return profit


#(profit, deadline, index)
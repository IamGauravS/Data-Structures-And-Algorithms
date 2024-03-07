def intervals_intersection(interval_list_a, interval_list_b):
    
    # Replace this placeholder return statement with your code
    lena = len(interval_list_a)
    lenb = len(interval_list_b)
    starta = 0
    startb = 0
    outputlist = []
    while starta < lena and startb < lenb:
        if interval_list_a[starta][0] > interval_list_b[startb][0]:
            startelem = interval_list_a[starta][0]
        else:
            startelem = interval_list_b[startb][0]

        if interval_list_a[starta][1] > interval_list_b[startb][1]:
            endelem = interval_list_b[startb][1]
            startb +=1
        else:
            endelem = interval_list_a[starta][1]
            starta +=1
        
        if endelem >= startelem:
            outputlist.append([startelem, endelem])
        

    return outputlist


##Let’s briefly discuss the approach that we have used to solve the above mentioned problem:

    Set two pointers, i and j, at the beginning of both lists, respectively, for their iteration.

    While iterating, find the latest starting time and the earliest ending time for each pair of intervals interval_list_a[i] and interval_list_a[j] .

    If the latest starting time is less than or equal to the earliest ending time, store it as an intersection.

    Increment the pointer (i or j) of the list having the smaller end time of the current interval.

    Keep iterating until either list is fully traversed.

    Return the list of intersections.

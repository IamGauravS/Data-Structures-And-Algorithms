def house_robber(money):
    if not money:
        return 0
    if len(money) == 1:
        return money[0]

    # Rob first house
    dp1 = [0 for _ in range(len(money))]
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1):  # Don't rob the last house
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # Rob last house
    dp2 = [0 for _ in range(len(money))]
    dp2[1] = money[1]
    for i in range(2, len(money)):  # Don't rob the first house
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(dp1[-2], dp2[-1])  # Return the maximum of the two results
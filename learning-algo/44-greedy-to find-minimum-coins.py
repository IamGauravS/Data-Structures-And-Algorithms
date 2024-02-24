def find_minimum_number_of_coins(value, coins):
    coins.sort()
    count = 0
    i = len(coins) -1
    while value != 0:
        if coins[i] > value:
            i -=1 
        else:
            value = value - coins[i]
            count +=1

    return count 
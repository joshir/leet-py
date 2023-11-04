def bruteforce(capacity, weights, profits):
    def dfs(index, capacity):
        if index == len(weights):
            return 0
        profit = dfs(index+1, capacity)
        if weights[index] <= capacity:
            choose = profits[index] + dfs(index+1, capacity - weights[index])
            profit = max(profit, choose)
        return profit

    dfs(0, capacity)


def memoized(capacity, weights, profits):
    memo = [[-1] * (capacity+1) for _ in range(len(weights))]

    def dfs(index, capacity):
        if index == len(weights):
            return 0
        if -1 != memo[index][capacity]:
            return memo[index][capacity] # you missed the whole point of this
        memo[index][capacity] = dfs(index + 1, capacity)
        if weights[index] <= capacity:
            choose = profits[index] + dfs(index + 1, capacity - weights[index])
            memo[index][capacity] = max(memo[index][capacity], choose)
        return memo[index][capacity]
    dfs(0, capacity)


def bup(capacity, weights, profits):

    dup = [[0] * (capacity+1) for _ in range(len(weights))]

    for curr_cap in range(capacity+1):
        if curr_cap >= weights[0]:
            dup[curr_cap] = profits[curr_cap]

    for i in range(len(weights)):
        dup[i][0] = 0

    for i in range (1, len(weights)):
        for curr_cap in range(1, capacity+1):
            forego = dup[i - 1][curr_cap]
            if curr_cap >= weights[i]:
                dup[i][curr_cap] = profits[i] + dup[i-1][curr_cap-weights[i]]
            dup[i][curr_cap]  = max(forego, dup[i][curr_cap])

    return dup[len(weights) - 1][capacity]

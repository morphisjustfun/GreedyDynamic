# knapsack greedy
def knapsackGreedy(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    value = 0.0
    weight = 0.0
    for item in items: # loop invariant
        if weight + item[0] <= capacity:
            value += item[1]
            weight += item[0]
    return value

# knapsack dynamic programming
def knapsackDP(items, capacity):
    value = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
    for i in range(1, len(items)+1):
        for j in range(1, capacity+1):
            if items[i-1][0] <= j:
                value[i][j] = max(value[i-1][j], value[i-1][j-items[i-1][0]] + items[i-1][1])
            else:
                value[i][j] = value[i-1][j]
    return value[len(items)][capacity]

# correctitud - si se puede

# test
def test():
    # items structure is (weight, value)
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    print(knapsackGreedy(items, capacity))
    print(knapsackDP(items, capacity))

if __name__ == '__main__':
    test()

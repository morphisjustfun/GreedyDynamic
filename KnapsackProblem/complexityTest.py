import time
import random
import matplotlib.pyplot as plt


def knapsackGreedyTest(items, capacity):
    selectedItems = []
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    currentValue = 0.0
    currentWeight = 0.0
    for item in items:  # loop invariant
        if currentWeight + item[0] <= capacity:
            selectedItems.append(item)
            currentValue += item[1]
            currentWeight += item[0]
    return currentValue, selectedItems


def knapsackBFTest(items, capacity):  # T(n) = nT(n-1) = O(n!)
    value = 0
    for i in range(len(items)):  # para cada item O(n)
        if items[i][0] <= capacity:  # si el peso es menor o igual al peso disponible
            value = max(value,
                        items[i][1] + knapsackBFTest(items[i + 1:],
                                                     capacity - items[i][0]))
    return value


def complexityTest(n, capacity):
    items = []
    for _ in range(n):
        items.append([random.randint(1, capacity), random.randint(1, 100)])

    # test execution time
    start = time.time()
    _, _ = knapsackGreedyTest(items, capacity)
    end = time.time()
    timeGreedy = end - start

    start = time.time()
    _ = knapsackBFTest(items, capacity)
    end = time.time()
    timeBF = end - start

    return timeGreedy, timeBF


def testKnapSack():
    executionTimes = {}
    for n in range(10, 90, 10):
        capacity = n // 1
        timeGreedy, timeBF = complexityTest(n, capacity)
        executionTimes[n] = [timeGreedy, timeBF]

    # plot with tags
    plt.plot(list(executionTimes.keys()), list(executionTimes.values()), label=['Naive','Greedy'])
    plt.xlabel('n')
    plt.ylabel('Execution Time')
    plt.title('Knapsack greedy vs naive approach')
    plt.legend(loc='best')
    plt.show()

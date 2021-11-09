from colorama import Fore
from complexityTest import testKnapSack


def prettyPrintData(items, capacity):
    print(Fore.RED + "Capacity:", end=" ")
    print(Fore.WHITE + str(capacity))
    print(Fore.RED + "Items:")
    for item in items:
        print(Fore.WHITE + Fore.YELLOW + "Weight", Fore.WHITE +
              str(item[0]), Fore.YELLOW + "Value", Fore.WHITE + str(item[1]))
    print()


def prettyPrintResult(value, selectedItems):
    print(Fore.RED + "Value:", end=" ")
    print(Fore.WHITE + str(value))
    print(Fore.RED + "Items:")
    for item in selectedItems:
        print(Fore.YELLOW + "Weight",
              Fore.WHITE + str(item[0]),
              Fore.YELLOW + "Value",
              Fore.WHITE + str(item[1]))



# overall complexity: O(n log n)
def knapsackGreedy(items, capacity):
    selectedItems = []
    # sort by value/weight ratio. The higher the ratio, the better the item.
    # Most valuable items are first.
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    # Sort complexity : O(n log n)
    prettyPrintData(items, capacity)
    currentValue = 0.0
    currentWeight = 0.0
    # Loop complexity : O(n)
    for item in items:  # loop invariant
        if currentWeight + item[0] <= capacity:
            selectedItems.append(item)
            currentValue += item[1]
            currentWeight += item[0]
    prettyPrintResult(currentValue, selectedItems)
    return currentValue, selectedItems

# correctitud - si se puede

# test
def testResult():
    # items structure is (weight, value)
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    knapsackGreedy(items, capacity)


if __name__ == '__main__':
    # testResult()
    testKnapSack()

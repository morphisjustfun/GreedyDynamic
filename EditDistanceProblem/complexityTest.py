import time
import random
import string


def naiveEditDistance(str1, str2, m, n):
    if m == 0:  # O(1)
        return n

    if n == 0:  # O(1)
        return m

    if str1[m - 1] == str2[n - 1]:  # O(1)
        return naiveEditDistance(str1, str2, m - 1, n - 1)  # T(n-1)

    return 1 + min(naiveEditDistance(str1, str2, m, n - 1),  # Insert
                   naiveEditDistance(str1, str2, m - 1, n),  # Remove
                   naiveEditDistance(str1, str2, m - 1, n - 1)  # Replace
                   )  # 3T(n-1)


def stringGenerator(length):
    result = ''.join(
        (random.choice(string.ascii_lowercase) for _ in range(length)))
    return result


def complexityTest(tamanho1, tamanho2):
    palabra1 = stringGenerator(tamanho1)
    palabra2 = stringGenerator(tamanho2)

    # test execution time
    start = time.time()
    editDistance = naiveEditDistance(palabra1, palabra2, tamanho1, tamanho2)
    end = time.time()
    timeNaive = end - start

    return editDistance, timeNaive


def testEditDistance():
    executionTimes = []
    naiveEditDistance = []
    for i in range(3, 7, 1):
        tamanho1 = i + 1
        tamanho2 = i + 2
        editDistance, timeNaive = complexityTest(tamanho1, tamanho2)
        executionTimes.append(timeNaive)
        naiveEditDistance.append(editDistance)
    return executionTimes, naiveEditDistance


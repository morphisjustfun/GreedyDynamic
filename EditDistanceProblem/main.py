from EditDistanceProblem.complexityTest import testEditDistance

if __name__ == '__main__':
    # testResult()
    executionTimes, naiveEditDistance = testEditDistance()
    print(executionTimes)
    print(naiveEditDistance)

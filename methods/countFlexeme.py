from const import constVariable


def Counter(sentence):
    table = constVariable.tableFlexeme
    i = 0
    result = []
    for itemType in table:
        counter = 0
        for item in itemType:
            counter += sentence.count('\'' + item)
        result += [constVariable.flags[i] + ': ' + ' ' + str(counter)]
        i += 1
    return result


def WriteToCounters(sentence):
    print(constVariable.pause)
    print("Analiza zdania: ")
    result = Counter(sentence)
    for item in result:
        print(item)


def WriteToCountersData(sentence):
    result = Counter(sentence)
    return result

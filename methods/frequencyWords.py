from const import constVariable
from pprint import pprint
from nltk.probability import FreqDist


def FrequencyWords(words):
    return FreqDist(words)


def TopMostWords(frequencyWords, topNumber):
    return frequencyWords.most_common(topNumber)


def FrequencyWordsString(words, topNumber):
    result = FrequencyWords(words)
    top = TopMostWords(result, topNumber)

    print(constVariable.pause)
    print("Czestotliwosc slow")
    print("Najczesciej wystepujace slowa: ")
    pprint(top)


def FrequencyWordsStringData(words, topNumber):
    result = FrequencyWords(words)
    top = TopMostWords(result, topNumber)
    return top



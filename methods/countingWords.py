from nltk.tokenize import word_tokenize
from const import constVariable


def FilterSentenceFromWords(text):
    return word_tokenize(text, "polish")


def CountSign(text):
    return len(text)


def CountWords(filterText):
    return [word for word in filterText if word not in constVariable.specialChar]


def CountSignAdnFilterString(text):
    filter = FilterSentenceFromWords(text)
    count = CountSign(filter)
    print(constVariable.pause)
    print("Liczba xyz:")
    print("W tekscie jest: " + str(count) + " slow i znakow.")
    return filter

def CounterWordsString(filterText):
    words = CountWords(filterText)
    print(constVariable.pause)
    print("Liczba slow:")
    print("W tekscie jest: " + str(len(words)) + " slow.")
    return words


def CountSignAdnFilterStringData(text):
    filter = FilterSentenceFromWords(text)
    count = CountSign(filter)
    return "W tekscie jest: " + str(count) + " slow i znakow."

def CounterWordsData(filterText):
    words = CountWords(filterText)
    return "W tekscie jest: " + str(len(words)) + " slow."

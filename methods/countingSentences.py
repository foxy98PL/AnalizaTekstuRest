from nltk.tokenize import sent_tokenize

pause = "------------------------------------------"


def CountSentence(text):
    return sent_tokenize(text, "polish")


def CountSentenceString(text):
    result = CountSentence(text)
    print(pause)
    print("Liczba zdan w tekscie: " + str(len(result)))
    return result

def CountSentenceStringData(text):
    result = CountSentence(text)
    return "Liczba zdan w tekscie: " + str(len(result))

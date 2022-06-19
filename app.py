from flask import Flask
from nltk.probability import FreqDist
import warnings
from methods import countFlexeme as cf, countingSentences as cs, countingWords as cw, dataManager as dm, \
    frequencyWords as fw, wordsAnalyzer as wa
from const import constVariable
import nltk
from flask import Flask, request, jsonify
app = Flask(__name__)
warnings.simplefilter(action='ignore', category=FutureWarning)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/analyse', methods=['POST'])
def foo():
    dataInput = request.json
    data = [jsonify(dataInput['text']).json]
    data = [data[0]]
    print(constVariable.pause)
    print("Analizowany tekst:")
    print(constVariable.pause)
    print(data[0])
    filter = cw.CountSignAdnFilterString(data[0])
    words = cw.CounterWordsString(filter)
    filterData = cw.CountSignAdnFilterStringData(data[0])
    wordsData = cw.CounterWordsData(filter)
    sentence = cs.CountSentenceString(data[0])
    sentenceData = cs.CountSentenceStringData(data[0])
    fw.FrequencyWordsString(words, 10)
    freqData = fw.FrequencyWordsStringData(words,10)
    tagWords = wa.TagWords(words)
    cf.WriteToCounters(str(tagWords))
    wa.TagWordsToPl(words)
    tagWordsPLData = wa.TagWordsToPlData(words)
    tagWordsData = cf.WriteToCountersData(str(tagWords))
    print(constVariable.pause)
    print(constVariable.line)
    print(constVariable.line)
    print(constVariable.line)
    print(constVariable.line + "Koniec Algorytmu" + constVariable.line)
    print(jsonify(data))
    return jsonify({
        "filterData" : filterData,
        "wordsData":wordsData,
        "sentenceData":sentenceData,
        "freqData": freqData,
        "tagWordsData": [tagWordsData,tagWordsPLData]
    })

if __name__ == '__main__':
    app.run()

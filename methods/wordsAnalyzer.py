from pprint import pprint

import treetaggerwrapper
import const.constVariable as cv
import re


def TagWords(words):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='pl')
    tags = tagger.tag_text(words)
    return treetaggerwrapper.make_tags(tags)


def TagWordsToPl(words):
    tags = TagWords(words)
    result = []
    for item in tags:
        split = str(item).split(',')
        patternName = "\'(.*?)\'"
        substring = re.search(patternName, str(split[0])).group(1)
        i = 0
        for flexeme in cv.tableFlexeme:
            for one in flexeme:
                if str(one) in str(split[1]):
                    result += [substring + ': ' + cv.flags[i]]
                    continue
            i += 1
    pprint(result)
def TagWordsToPlData(words):
    tags = TagWords(words)
    result = []
    for item in tags:
        split = str(item).split(',')
        patternName = "\'(.*?)\'"
        substring = re.search(patternName, str(split[0])).group(1)
        i = 0
        for flexeme in cv.tableFlexeme:
            for one in flexeme:
                if str(one) in str(split[1]):
                    result += [substring + ': ' + cv.flags[i]]
                    continue
            i += 1
    return result

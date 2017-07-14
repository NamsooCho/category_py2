#! /usr/bin/python3
# -*- coding: utf-8 -*-

import konlpy
import nltk
from dao import Dao

grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VP: {<V.*>*}            # Verb phrase
AP: {<A.*>*}            # Adjective phrase
"""
parser = nltk.RegexpParser(grammar)

dao = Dao()
rows = dao.GetBeforeText()

for row in rows:
    sentence = row[0]
    after = ''
    words = konlpy.tag.Twitter().pos(sentence)

    chunks = parser.parse(words)
    for subtree in chunks.subtrees():
        if subtree.label()=='NP':
            after = after + " " + ' '.join((e[0] for e in list(subtree)))
    dao.SaveAfterProcessing(after, row[1])

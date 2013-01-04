#!/usr/bin/env python

"""
sent-suggest.py: Generates an alernative sentence by looking up synonyms for particlar words based on their part of speech.
This was inspired by an email I received which I have used as the initial example text.
"""

__author__      = "Shankar Ambady"
__copyright__   = "Copyright 2012, sambady@sessionm.com"


from nltk import ne_chunk,pos_tag
from nltk import ne_chunk,pos_tag
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.corpus import stopwords

text = '''

Hello Shankar, 

My name is Walter White and I was watching your NLP in Python video on YouTube and had some questions as well as a request from you. 

My first question: 
Would it be possible, through NLP, to have a computer suggest changes or variants to a sentence based on certain key points in a sentence. Similar to the way Summly summarizes a full body of work by pulling out key pieces. I was wondering if this was possible by pulling out the subject, main verb and key adjectives. So, for example: 
The cat drank the milk.
NLP variant: The cat (lapped, drank, sipped) (up) the milk (ferociously, with much appreciation, with a hungry intent). 

So essentially, what the program should do is act as a sentence thesaurus, suggesting bonus adjective phrases to a sentence as well as building a thesaurus type response that would input phrase variations. In an extremely simplistic 100% prototype kind of way, is this possible?

My second question is: Can, through NLP, a program find flaws in a sentence? I know Microsoft Word can find fragments, and every app can basically find spelling errors and thesaurus's are already real, but is there a way for a program, running Python, to find sentence variants based on a sentence weak sound? So if a sentence just isn't strong, can a program understand that and change that?

My request now is, would you be willing to help me better understand Python and NLP through a sort of email back and forth, share code kind of way? 

I have an idea and I really want to build it and I think the plausibility of it working is there.

The idea is essentially to thesaurus sentences from essays submitted by any person. So a person, without an actual account or anything (I'd rather save all the extra difficulty for down the line) can come on plug their essay into a text field, click submit and the essay comes up in a box and you click on sentence and a box next to it gives you variants to a sentence. Is that possible and if so, how would I begin going about doing it? 

I hope you consider helping me,
Thanks,
Walter White


'''
import nltk.data
from nltk.corpus import wordnet


def find_synonym(word,pos):
    l_syns = []
    synsets = wordnet.synsets(word,pos=pos)
    for synset in synsets:
      for syn in synset.lemma_names:
        l_syns.append(syn)
    return l_syns
    

stopwords = stopwords.words('english') # common english words to filter out

TreeBankTokenizer = TreebankWordTokenizer()

PunktTokenizer = PunktSentenceTokenizer()

sentences = nltk.sent_tokenize(text)

tokens = [nltk.wordpunct_tokenize(sentence) for sentence in sentences]

tagged = [pos_tag(token) for token in tokens]

changedstr = []
inlinestr = []

for taggedsentence in tagged:
  for postagged in taggedsentence:
    word = postagged[0]
    postag = postagged[1][0].lower()
    synonyms = []
    try:
      synonyms  = find_synonym(word.lower(),postag)
    except:
      pass
    inlinestr.append(postagged[0])
    if(len(synonyms) > 0):
      word = synonyms[0]
      inlinestr.extend([' (' ,','.join(synonyms) ,')'])
    changedstr.append(word)
    
changedstr = ' '.join(changedstr)
inlinestr = ' '.join(inlinestr)

print "ORIGINAL TEXT: \n" + text + "\n\n"

print "ALTERNATE TEXT: \n" + changedstr  + "\n\n"


print "\n\nINLINE CHANGES: \n" + inlinestr  + "\n\n"

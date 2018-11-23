# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 00:42:58 2018

@author: Jie Lu
"""

#download data with nltk gutenberg
import nltk
import numpy as np
nltk.download('gutenberg')
nltk.download('punkt')
from nltk.corpus import gutenberg

book1 = gutenberg.sents('milton-paradise.txt')[:1000]
book2 = gutenberg.sents('shakespeare-macbeth.txt')[:1000]
book3 = gutenberg.sents('bible-kjv.txt')[:1000]
books = book1 + book2 + book3

x_train = []
y_train = [0]*1000 + [1]*1000 + [2]*1000

for i in range(len(books)):
  temp = ' '.join(word for word in books[i])
  x_train.append(temp)
  
#shuffle x and y
x_train, y_train = np.array(x_train), np.array(y_train)

def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]
  
x_train, y_train = unison_shuffled_copies(x_train, y_train)

#tokenize x
max_len = 30
num_words = 1000
from keras.preprocessing.text import Tokenizer
# Fit the tokenizer on the training data
t = Tokenizer(num_words=num_words)
t.fit_on_texts(x_train)

#saved in metadata
metadata = {
  'word_index': t.word_index,
  'max_len': max_len,
  'vocabulary_size': num_words,
}

#pad sequence
x_train = t.texts_to_sequences(x_train)
x_train = pad_sequences(x_train, maxlen=max_len, padding='post')
# print(x_train)



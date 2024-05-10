# -*- coding: utf-8 -*-
"""S6-formativa-pln-Thrones2Vec.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1epRMe2VacDn4mTel_6Fzhchhn6DoHZJ1

# Thrones2Vec

© Yuriy Guts, 2016

Using only the raw text of [A Song of Ice and Fire](https://en.wikipedia.org/wiki/A_Song_of_Ice_and_Fire), we'll derive and explore the semantic properties of its words.

## Imports
"""

# Usado em inicio de script python2, ajuda a escrever código compatível com Python 2 e Python 3
from __future__ import absolute_import, division, print_function

import codecs
import glob
import logging
import multiprocessing
import os
import pprint
import re

import nltk
import gensim.models.word2vec as w2v
import sklearn.manifold
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline

"""**Set up logging**"""

# Configura sistema de logging para imprimir mensagens no formato especificado, com data e hora, nível
# de log e conteúdo da mensagem, e apenas mensagens com nível INFO ou superior serão exibidas
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

"""**Download NLTK tokenizer models (only the first time)**"""

nltk.download("punkt")
nltk.download("stopwords")

"""## Prepare Corpus

**Load books from files**
"""

# Colocar arquivos txt em pasta data nos Arquivos do Google Colab
book_filenames = sorted(glob.glob("data/*.txt"))

print("Found books:")
book_filenames

"""**Combine the books into one string**"""

corpus_raw = u""
for book_filename in book_filenames:
    print("Reading '{0}'...".format(book_filename))
    with codecs.open(book_filename, "r", "utf-8") as book_file:
        corpus_raw += book_file.read()
    print("Corpus is now {0} characters long".format(len(corpus_raw)))
    print()

"""**Split the corpus into sentences**"""

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

raw_sentences = tokenizer.tokenize(corpus_raw)

#convert into a list of words
#rtemove unnnecessary,, split into words, no hyphens
#list of words
def sentence_to_wordlist(raw):
    clean = re.sub("[^a-zA-Z]"," ", raw)
    words = clean.split()
    return words

#sentence where each word is tokenized
sentences = []
for raw_sentence in raw_sentences:
    if len(raw_sentence) > 0:
        sentences.append(sentence_to_wordlist(raw_sentence))

print(raw_sentences[5])
print(sentence_to_wordlist(raw_sentences[5]))

# Contagem de tokens do corpus
token_count = sum([len(sentence) for sentence in sentences])
print("The book corpus contains {0:,} tokens".format(token_count))

"""## Train Word2Vec"""

#ONCE we have vectors
#step 3 - build model
#3 main tasks that vectors help with
#DISTANCE, SIMILARITY, RANKING

# Dimensionality of the resulting word vectors.
#more dimensions, more computationally expensive to train
#but also more accurate
#more dimensions = more generalized
num_features = 300
# Minimum word count threshold.
min_word_count = 3

# Number of threads to run in parallel.
#more workers, faster we train
num_workers = multiprocessing.cpu_count()

# Context window length.
context_size = 7

# Downsample setting for frequent words.
#0 - 1e-5 is good for this
downsampling = 1e-3

# Seed for the RNG, to make the results reproducible.
#random number generator
#deterministic, good for debugging
seed = 1

# Cria modelo Word2Vec com as configurações especificadas e o armazena na variável thrones2vec.
# Modelo será treinado com os parâmetros fornecidos e será capaz de representar palavras em
# vetores de alta dimensão, capturando relações semânticas e contextuais entre elas.
thrones2vec = w2v.Word2Vec(
    sg=1,
    seed=seed,
    workers=num_workers,
    vector_size=num_features,
    min_count=min_word_count,
    window=context_size,
    sample=downsampling
)

thrones2vec.build_vocab(sentences)

# print("Word2Vec vocabulary length:", len(thrones2vec.vocab)) - obsoleto
# print("Word2Vec vocabulary length:", len(thrones2vec.wv.vocab)) - obsoleto

print("Word2Vec vocabulary length:", len(thrones2vec.wv.key_to_index))

"""**Start training, this might take a minute or two...**"""

# thrones2vec.train(sentences)
thrones2vec.train(sentences, total_examples=thrones2vec.corpus_count, epochs=30)

"""**Save to file, can be useful later**"""

if not os.path.exists("trained"):
    os.makedirs("trained")

thrones2vec.save(os.path.join("trained", "thrones2vec.w2v"))

"""## Explore the trained model."""

thrones2vec = w2v.Word2Vec.load(os.path.join("trained", "thrones2vec.w2v"))

"""### Compress the word vectors into 2D space and plot them"""

#my video - how to visualize a dataset easily
tsne = sklearn.manifold.TSNE(n_components=2, random_state=0)

# all_word_vectors_matrix = thrones2vec.syn0 - obsoleto
all_word_vectors_matrix = thrones2vec.wv.vectors

"""**Train t-SNE, this could take a minute or two...**"""

all_word_vectors_matrix_2d = tsne.fit_transform(all_word_vectors_matrix)

"""**Plot the big picture**"""

points = pd.DataFrame(
    [
        (word, coords[0], coords[1])
        for word, coords in [
            (word, all_word_vectors_matrix_2d[thrones2vec.wv.key_to_index[word]])
            for word in thrones2vec.wv.key_to_index
        ]
    ],
    columns=["word", "x", "y"]
)

points.head(10)

sns.set_context("poster")

points.plot.scatter("x", "y", s=10, figsize=(20, 12))

"""**Zoom in to some interesting places**"""

def plot_region(x_bounds, y_bounds):
    slice = points[
        (x_bounds[0] <= points.x) &
        (points.x <= x_bounds[1]) &
        (y_bounds[0] <= points.y) &
        (points.y <= y_bounds[1])
    ]

    ax = slice.plot.scatter("x", "y", s=35, figsize=(10, 8))
    for i, point in slice.iterrows():
        ax.text(point.x + 0.005, point.y + 0.005, point.word, fontsize=9)

"""**People related to Kingsguard ended up together**"""

#plot_region(x_bounds=(4.0, 4.2), y_bounds=(-0.5, -0.1))
plot_region(x_bounds=(-2, 0), y_bounds=(0, 2))

"""**Food products are grouped nicely as well. Aerys (The Mad King) being close to "roasted" also looks sadly correct**"""

plot_region(x_bounds=(0, 3), y_bounds=(3, 3.5))

"""### Explore semantic similarities between book characters

**Words closest to the given word**
"""

thrones2vec.wv.most_similar("Stark")

thrones2vec.wv.most_similar("Aerys")

thrones2vec.wv.most_similar("direwolf")

"""**Linear relationships between word pairs**"""

def nearest_similarity_cosmul(start1, end1, end2):
    similarities = thrones2vec.wv.most_similar_cosmul(
        positive=[end2, start1],
        negative=[end1]
    )
    start2 = similarities[0][0]
    print("{start1} is related to {end1}, as {start2} is related to {end2}".format(**locals()))
    return start2

nearest_similarity_cosmul("Stark", "Winterfell", "Riverrun")
nearest_similarity_cosmul("Jaime", "sword", "wine")
nearest_similarity_cosmul("Arya", "Nymeria", "dragons")
#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print 'usage: %s <letters> [wordlistfile]' % sys.argv[0]
    exit(2)

letters = str(sys.argv[1])

if len(sys.argv) > 2:
    wordlist = str(sys.argv[2])
else:
    wordlist = 'wordlist'

with open(wordlist) as f:
    words = filter(len, [line.strip() for line in f.readlines()])

def letter_freq(word):
    lf = {}
    for l in word:
        lf[l] = lf.get(l, 0) + 1
    return lf

word_letter_freq = {word: letter_freq(word) for word in words}

def search(letters):
    l_freq = letter_freq(letters)

    match = []
    for w, w_l_freq in word_letter_freq.iteritems():
        hit = True
        for l in w:
            if l_freq.get(l, 0) < w_l_freq[l]:
                hit = False
                break
        if hit:
            match.append(w)

    return match


matches = search(letters)
for each in sorted(matches, key=len):
    print each

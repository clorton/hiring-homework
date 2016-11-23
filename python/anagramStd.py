#!/usr/bin/python

from __future__ import print_function
import argparse
from collections import defaultdict
from OrderedSet import OrderedSet


class Anagrams:
    def __init__(self, wordlist):
        self.__anagrams__ = defaultdict(OrderedSet)
        with open(wordlist, 'r') as handle:
            for word in handle:
                word = word.strip()
                key = Anagrams.__key__(word)
                self.__anagrams__[key].add(word)
        return

    def __getitem__(self, item):
        key = Anagrams.__key__(item)
        return self.__anagrams__[key] if key in self.__anagrams__ else []

    @staticmethod
    def __key__(word):
        return ''.join(sorted(list(word.lower())))


def main(wordlist, words):
    anagrams = Anagrams(wordlist)
    process_words(words, anagrams)
    return


def process_words(words, anagrams):
    for word in words:
        print("Anagrams of '{0}':".format(word))
        matches = anagrams[word]
        if len(matches) > 0:
            for entry in matches:
                print('\t{0}'.format(entry))
        else:
            print('\tNo anagrams found.')
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('wordlist')
    parser.add_argument('words', nargs='+')
    args = parser.parse_args()

    main(args.wordlist, args.words)

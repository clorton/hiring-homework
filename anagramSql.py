#!/usr/bin/python

from __future__ import print_function
import argparse
import sqlite3


class Anagrams:
    def __init__(self, wordlist):
        self.__connection__ = sqlite3.connect(':memory:')
        self.__cursor__ = self.__connection__.cursor()
        self.__cursor__.execute("CREATE TABLE anagrams (key text, word text)")
        with open(wordlist, 'r') as handle:
            for word in handle:
                word = word.strip()
                key = Anagrams.__key__(word)
                self.__cursor__.execute('INSERT INTO anagrams VALUES (?, ?)', (key, word))
        self.__connection__.commit()
        self.__cursor__.execute('CREATE INDEX keys ON anagrams(key)')
        self.__connection__.commit()
        return

    def __getitem__(self, item):
        key = Anagrams.__key__(item)
        # Use [key] rather than (key) because (key) isn't a tuple and (key,) looks weird.
        return [row[0] for row in self.__cursor__.execute('SELECT word FROM anagrams WHERE key=? ORDER BY word', [key])]

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

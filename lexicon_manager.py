#!/usr/bin/env python3

class Manager:
    def __init__(self):
        self.lexicon = Lexicon()
        return

    def read_file(self, filename):
        with open(filename, 'r') as fh:
            x = fh.readline()
        return x

class Lexicon:
    def __init__(self):
        self._words = []
        self._current_word = 0
        return

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._words) != 0 and self._current_word <= len(self._words):
            self._current_word += 1
            return self._words[self._current_word]
        else:
            raise StopIteration

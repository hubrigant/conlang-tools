#!/usr/bin/env python3

import json
from lexifer.PhDefParser import PhonologyDefinition
from lexifer.wordgen import SoundSystem


class Manager:
    def __init__(self):
        self.lexicon = Lexicon()
        return

    def read_file(self, filename):
        with open(filename, 'r') as fh:
            self.lexicon.add(json.loads(fh.read()))

    def write_file(self, filename):
        with open(filename, 'w') as fh:
            fh.write(json.dumps(str(self.lexicon)))

    def lexifer(self, config):
        self.lexifer_obj = PhonologyDefinition(SoundSystem(),
                                               opthash=config)
        return self.lexifer_obj


class Lexicon:
    def __init__(self):
        self._words = []
        self._current_word = 0
        return

    def __iter__(self):
        yield self

    def __len__(self):
        return len(self._words)

    def __next__(self):
        if len(self._words) != 0 and self._current_word <= len(self._words):
            self._current_word += 1
            return self._words[self._current_word]
        else:
            raise StopIteration

    def __str__(self):
        return str(self._words)

    def add(self, word_list):
        for word in word_list:
            self._words.append(word)

    def remove(self, word_key, word_value):
        for idx, entry in enumerate(self._words):
            if entry[word_key] == word_value:
                try:
                    self._words.pop(idx)
                except ValueError:
                    continue
        return

    def get_word(self, key, value, match_whole_word=False):
        results = [entry for idx, entry in enumerate(self._words)
                   if entry[key] == value]
        return results

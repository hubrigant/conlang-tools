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
        #  return self._words.append({'lang_word': lang_word,
        #                             'local_word': local_word,
        #                             'PoS': PoS})

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

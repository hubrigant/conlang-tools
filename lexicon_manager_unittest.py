#!/usr/bin/env python3

import unittest
#  from expects import *
#  from unittest.mock import patch, mock_open
from lexicon_manager import Manager, Lexicon
from collections.abc import Iterable


class TestManagerClass(unittest.TestCase):

    def setUp(self):
        self.mgr = Manager()
        self.lex = Lexicon()
        self.lex.add("abc", "def", "noun")
        self.lex.add("xyz", "ghi", "noun")
        self.lex.add("abcxyz", "ghi", "noun")

    def test_classness(self):
        self.assertIsInstance(self.mgr, Manager,
                              "mgr object isn't an instance of Manager")

    def test_data_structure_creation(self):
        mgr = Manager()
        self.assertIsInstance(mgr.lexicon, Lexicon,
                              "Manager's data structure isn't a Lexicon class")
        self.assertIsInstance(mgr.lexicon, Iterable)
        self.assertEqual(len(mgr.lexicon), 0,
                         "Manager's lexicon length isn't initially 0")

    def test_data_structure_add(self):
        lex = Lexicon()
        lex.add("abc", "def", "noun")
        self.assertEqual(len(lex), 1,
                         "Manager's lexicon length isn't 1 after add()")
        self.lex.add("xyz", "ghi", "noun")

    def test_data_structure_remove(self):
        lex = Lexicon()
        lex.add("abc", "def", "noun")
        lex.remove("lang_word", "abc")
        self.assertEqual(len(lex), 0,
                         "Manager's lexicon length isn't initially 0")

    def test_data_structure_querie_by_lang_word(self):
        self.assertEqual([{'lang_word': 'abc',
                           'local_word': 'def',
                           'PoS': 'noun'}],
                         self.lex.get_word('lang_word',
                                           'abc'))

    def test_data_structure_query_by_local_word(self):
        self.assertEqual([{'lang_word': 'abc',
                           'local_word': 'def',
                           'PoS': 'noun'}],
                         self.lex.get_word('local_word',
                                           'def'))

    def test_data_structure_query_match_whole_word(self):
        self.assertEqual([{'lang_word': 'xyz',
                           'local_word': 'ghi',
                           'PoS': 'noun'}],
                         self.lex.get_word('lang_word',
                                           'xyz',
                                           match_whole_word=True))

#  with description("<Hooks>") as self:
#      with before.each:
#          self.manager = Manager()
#          self.datastore = 'language1.lmgr'
#          with it("has file management capapbilities"):
#              @patch('Manager.open') #, mock_open(read_data='abc\n'))
#              expect(self.manager).to(have_property('read_file'))
#              expect(self.manager.read_file).to(be_callable)
#              expect(self.manager.read_file(self.datastore).to(equal("abc\n")))


if __name__ == '__main__':
    unittest.main()

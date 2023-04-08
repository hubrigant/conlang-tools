#!/usr/bin/env python3

import unittest
from unittest.mock import patch, mock_open
from lexicon_manager import Manager, Lexicon
from collections.abc import Iterable


class TestManagerClass(unittest.TestCase):

    def setUp(self):
        self.mgr = Manager()
        self.lex = Lexicon()
        add_words = [
            {'lang_word': 'abc',
             'local_word': 'def',
             'PoS': 'noun'},
            {'lang_word': 'xyz',
             'local_word': 'ghi',
             'PoS': 'noun'},
            {'lang_word': 'abcxyz',
             'local_word': 'defghi',
             'PoS': 'verb'}]
        self.lex.add(add_words)

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
        add_words = [
            {'lang_word': 'abc',
             'local_word': 'def',
             'PoS': 'noun'},
            {'lang_word': 'xyz',
             'local_word': 'ghi',
             'PoS': 'noun'},
            {'lang_word': 'abcxyz',
             'local_word': 'defghi',
             'PoS': 'verb'}
        ]
        lex.add(add_words)
        self.assertEqual(len(lex), 3,
                         "Manager's lexicon length isn't 3 after add()")

    def test_data_structure_remove(self):
        self.lex.remove("lang_word", "abc")
        self.assertEqual(len(self.lex), 2,
                         "Manager's lexicon length isn't 2 after remove")

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

        def test_data_file_read(self):
            with patch('__main__.open',
                       mock_open(read_data=self.add_words)) as m:
                with open('foo') as h:
                    result = h.read()

            m.assert_called_once_with('foo')
            assert result == self.add_words

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

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

    def test_classness(self):
        self.assertIsInstance(self.mgr, Manager,
                              "mgr object isn't an instance of Manager")

    def test_data_structure(self):
        self.assertIsInstance(self.mgr.lexicon, Lexicon,
                              "Manager's data structure isn't a Lexicon class")
        self.assertIsInstance(self.mgr.lexicon, Iterable)
        self.assertEquals(len(self.mgr.lexicon), 0,
                          "Manager's lexicon length isn't initially 0")
        self.lex.add("abc", "def", "noun")
        self.assertEquals(len(self.lex), 1,
                          "Manager's lexicon length isn't 1 after add()")
        print(self.lex)
        self.lex.add("xyz", "ghi", "noun")
        print(self.lex)
        self.assertEquals('def', self.lex.get_word_by_lang('def'))
        self.lex.remove("lang_word", "abc")
        self.assertEquals(len(self.mgr.lexicon), 0,
                          "Manager's lexicon length isn't initially 0")
        print(self.lex)


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

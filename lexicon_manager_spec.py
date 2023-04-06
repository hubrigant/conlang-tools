#!/usr/bin/env python3

from mamba import *
from expects import *
from unittest.mock import patch, mock_open
from lexicon_manager import Manager, Lexicon
from collections.abc import Iterable

with description("<Hooks>") as self:
    with before.each:
        self.manager = Manager()
        self.datastore = 'language1.lmgr'
    with description("Class tests:") as self:
        with it("starts as a basic class"):
            expect(self.manager).to(be_a(Manager))
        with it("has file management capapbilities"):
            @patch('Manager.open') #, mock_open(read_data='abc\n'))
            expect(self.manager).to(have_property('read_file'))
            expect(self.manager.read_file).to(be_callable)
            expect(self.manager.read_file(self.datastore).to(equal("abc\n")))
        with it("has the data structure"):
            expect(self.manager.lexicon).to(be_a(Lexicon))
            expect(self.manager.lexicon).to(have_length(0))
            expect(self.manager.lexicon).to(be_an(Iterable))

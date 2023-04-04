#!/usr/bin/env python3

from mamba import description, context, it
from expects import expect, equal
from lexicon_manager import manager

with description("Class") as self:
    with it("starts as a basic class"):
        manager = Manager()

        expect(type(manager)).to(equal("Manager"))

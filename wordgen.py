#!/usr/bin/env python3

from Zompist import Zompist

zomp = Zompist(maxRecurse=500,
               rawCategories='C=bcdfg\nV=aeiou',
               monosyllableRarity=1.0,
               rawSyllables='CV\nV',
               rawRewriteValues='',
               rawIllegalClusters='ba')

print(zomp.genWords(lexiconLength=10))

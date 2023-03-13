#!/usr/bin/env python3

from Zompist import Zompist

zomp = Zompist(dropoff=15,
               maxRecurse=500,
               rawCategories='C=bcdfg\nV=aeiou',
               monosyllableRarity=1.0,
               rawSyllables='CV\nV',
               rawRewriteValues='',
               rawIllegalClusters='')

print(zomp.genWords(lexiconLength=10))

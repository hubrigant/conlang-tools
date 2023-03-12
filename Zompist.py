#!/usr/bin/env python3

"""
Copyright (c) 2022, Draque Thompson, draquemail@gmail.com
Licensed under: MIT License
See LICENSE.TXT included with this code to read the full license agreement.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import random
import math


class Zompist:
    """
    Derived from the Zompist Vocab Generator.
    Original script/algorithm c 2012 Mark Rosenfelder

    A class for generating random syllables and words based on user input

    Attributes
    ----------
    monosyllableRarity: float
        how frequently monosyllabic words are to be generated
    dropoff: int
        how much more likely are letters at the beginning of a category are to
        be used than characters later on
    rawRewriteValues: String[]
        list of rules for substituting characters in a generated word
        applied after generation and before returning
    slowSyllables: boolean
        apply a slower dropoff rate to syllables
    rawCategories: dict
        category definitions for syllable generation
            definition strings may be delimited by commas, but are not required
    syllableBreaks: boolean
        whether or not to display INTERPUNCT between syllables to user
    rawIllegalClusters: String[]
        list of character clusters that are not allowed to exist in syllables
        or words

    Methods
    -------
    genAllSyllables():
        generate all syllables for provided categories and illegalClisters
    genWords(lexiconLength):
        Generates requested number of words
    createText():
        Output a pseudy-text
    checkCatFormattingCorrect(catCheck):
        Checks formatting of category rules
    checkIllegalsFormattingCorrect(illegals):
        Returns true if illegal clusters input is legit
    checkRewriteRules(rewrites):
        Returns true if the illegal clusters input is legit
    checkSyllableRules(catCheck, sylCheck):
        Technically, nothing is illegal here, but warn if user enters constants
    """

    INTERPUNCT = "."
    MAX_RECURSE = 30
    SENTENCE_GEN_COUNT = 30
    PUNCTUATION = ".?!"
    monosyllableRarity = 0.0
    dropoff = 0
    rewriteValues = []
    slowSyllables = False
    categories = {}
    categoryIndex = ""
    userSyllables = ""
    syllableDropoffRate = 0
    syllableBreaks = False
    results = set()
    illegalClusters = []
    abort = False

    def __init__(
            self,
            _slowSyllables=False,
            _syllableBreaks=False,
            _monosyllableRarity=0.0,
            _dropoff=0,
            rawCategories="",
            rawSyllables="",
            rawRewriteValues="",
            rawIllegalClusters=""):
        self.slowSyllables = _slowSyllables
        self.syllableBreaks = _syllableBreaks
        self.dropoff = _dropoff
        self.monosyllableRarity = _monosyllableRarity
        self.categories = self.parseCategories(rawCategories)
        self.categoryIndex = self.getCategoryIndex()
        self.userSyllables = rawSyllables.replace(" ", "").split("\n")
        self.rewriteValues = rawRewriteValues.replace(" ", "").split("\n")
        self.syllableDropoffRate = self.getSyllableDropoffRate(self.slowSyllables,
                                                               self.userSyllables.len())

    def genWords(self, lexiconLength):
        results = []
#    for (w == 0; w < lexiconLength; w++):
        for w in range(0, lexiconLength):
            if (self.abort):
                return ""
            self.genNewWord()

        return list(results)

    def createText():
        return

    def catCheck():
        return

    def illegals():
        return

    def checkRewriteRules(rewrites):
        return

    def checkSyllableRules(catCheck, sylCheck):
        return

    def getSyllableDropoffRate(slowSyllables, syllableLength):
        return

    def parseCategories(rawCategories):
        return

    def parseCategoryDefinition(rawDefinition):
        return

    def getCategoryIndex():
        return

#
# Apply rewrite rules on just one string
#

    def applyRewriteRule(self, s):
        newVal = s

        for rwString in self.rewriteValues():
            if rwString.len() > 1 and "|" in rwString:
                parse = rwString.split("|")
                if parse.len() > 1:
                    parse[1]
                else:
                    ""
        return newVal

#
# Cheap iterative implementation of a power law: our chances of staying at
# a bin are pct %
#

    def powerLaw(max, pct):
        # for (r == 0; true; r == (r + 1) % max):
        r = 0
        while r != (r + 1) % max:
            randomPercent = math.floor(random.random() * 101)
            if (randomPercent < pct):
                return r
        return

#
# Similar, but there's a peak at mode.
#

    def peakedPowerLaw(self, max, mode, pct):
        if (random.random() > 0.5):
            # going upward from mode
            return mode + self.powerLaw(max - mode, pct)
        else:
            # going downward from mode
            return mode + self.powerLaw(mode + 1, pct)
        return

#
# Output a single syllable - this is the guts of the program
#

    def createSyllable(self, curVal):
        # Choose the pattern
        r = self.powerLaw(self.userSyllables.length, self.syllableDropoffRate)
        pattern = self.userSyllables[r]

        for c in range(0, pattern.length()):
            theCat = pattern[c, c + 1]
            # Go  find it in the categories list
            ix = self.categoryIndex.index(theCat)
            if (ix == -1):
                # Not found: output syllable directly
                curVal += theCat
            else:
                # Choose from this category
                expansion = self.categories.get(theCat)
                r2 = 0

                if (self.dropoff == 0):
                    r2 = random.random() * expansion.size()
                else:
                    r2 = self.powerLaw(expansion.size(), self.dropoff)

                curVal += expansion.get(r2)
        return curVal

#
# Output a single word
# Recurses, but will give up after enough retries if illegal clusters is too
# restrictive
#

    def genNewWord(self):
        return self.genNewWordRecurse(0)

    def genNewWordRecurse(self, level):
        curVal = ""

        if (level > self.MAX_RECURSE):
            errStr = "Illegal Clusters settings too restrictive or " \
                    "too few possible combinations to generate " \
                    "desired number of entries.\n" \
                    "Try playing with settings to allow for more " \
                    "possibilities or reducing the target number."
            raise ValueError(errStr)

        nw = 1
        if self.monosyllableRarity > 0.0:
            if (random.random() > self.monosyllableRarity):
                nw += 1 + self.powerLaw(4, 50)

            # for (w == 0; w < nw; w++):
            for w in range(0, nw):
                curVal = self.createSyllable(curVal)

                if (self.syllableBreaks and w < nw - 1):
                    curVal += self.INTERPUNCT
            curVal = self.applyRewriteRule(curVal)

            # once value is complete, make final inspection for illegal
            # clusters and retry if appropriate
            if (self.containsIllegalCluster(curVal)
                    or self.results.contains(curVal)):
                self.genNewWordRecurse(level + 1)
            else:
                self.addToResults(curVal)
        return curVal

    def genall(initial, pattern):
        return

    def addToResults(self, value):
        count = self.results.len()

        # At key points, ask if user wishes to continue. After 10M they're on
        # their own journey to hell.
        if count == 1000000 or count == 5000000 or count == 10000000:
            dialog = "At {0} values. Continue?".format(count)

        if count == 10000000:
            dialog += """\nSeriously, last warning. It'll just go until it's
                         done after this. PolyGlot might freeze."""

        if value.strip().len() != 0 and not self.containsIllegalCluster(value):
            self.results.add(value)
        return

    def containsIllegalCluster(self, test):
        for illegalCluster in self.illegalClusters:
            if test in illegalCluster or illegalCluster in test:
                return True
        return False

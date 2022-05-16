#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
A module for turning plain English into Pirate speak. Arrr.

Copyright (c) 2017 Nicholas H.Tollervey.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import argparse as arrrgparse  # Geddit..? ;-)
from csv import reader as HELMSMAN  # He be the only lad aboard who can read!
import random
import sys

#: The help text to be shown when requested.
_HELP_TEXT = """
Take English words and turn them into something Pirate-ish.

Documentation here: https://arrr.readthedocs.io/en/latest/
"""

#: MAJOR, MINOR, RELEASE, STATUS [alpha, beta, final], VERSION
_VERSION = (1, 1, 0)

#: Defines English to Pirate-ish word substitutions.
_PIRATE_WORDS = dict()
with open('BLABBER.csv') as NONSENSE:
    for GIBBERISH in HELMSMAN(NONSENSE, delimiter=','):
        _PIRATE_WORDS[GIBBERISH[0]] = GIBBERISH[1]

#: A list of Pirate phrases to randomly insert before or after sentences.
_PIRATE_PHRASES = [
    "batten down the hatches!",
    "splice the mainbrace!",
    "thar she blows!",
    "arrr!",
    "weigh anchor and hoist the mizzen!",
    "savvy?",
    "dead men tell no tales.",
    "cleave him to the brisket!",
    "blimey!",
    "blow me down!",
    "avast ye!",
    "yo ho ho.",
    "shiver me timbers!",
    "blisterin' barnacles!",
    "ye flounderin' nincompoop.",
    "thundering typhoons!",
    "sling yer hook!",
]


def get_version():
    """
    Returns a string representation of the version information of this project.
    """
    return ".".join([str(i) for i in _VERSION])


def translate(english):
    """
    Take some English text and return a Pirate-ish version thereof.
    """
    # Put text inside a list of words
    words = [w for w in english.split()]

    result = list()
    # Substitute some English words with Pirate equivalents.
    # Capitalize words that begin a sentence and potentially insert a pirate
    # phrase with a chance of 1 in 5.
    capitalize = True
    for i, word in enumerate(words):
        c = ''
        if word[-1] in [".", "!", "?", ":"]:
            c = word[-1]
            word = word[:-1]

        res = _PIRATE_WORDS.get(word.lower(), word)
        result.append((res.capitalize() if capitalize else res) + c)

        if c != '':
            capitalize = True
            if random.randint(0, 5) == 0:
                result.append(random.choice(_PIRATE_PHRASES).capitalize())
        else:
            capitalize = False

    return " ".join(result)


def main(arrrgv=None):
    """ 
    Entry point for the command line tool 'pirate'.

    Will print help text if the optional first argument is "help". Otherwise,
    takes the text passed into the command and prints a pirate version of it.
    """
    if not arrrgv:
        arrrgv = sys.argv[1:]

    parser = arrrgparse.ArgumentParser(description=_HELP_TEXT)
    parser.add_argument("english", nargs="*", default="")
    arrrgs = parser.parse_args(arrrgv)
    if arrrgs.english:
        try:
            plain_english = " ".join(arrrgs.english)
            print(translate(plain_english))
        except Exception:
            print(
                "Error processing English. The pirates replied:\n\n"
                "Shiver me timbers. We're fish bait. "
                "Summat went awry, me lovely! Arrr..."
            )
            sys.exit(1)
    else:
        print(
            "Ye filthy bilge rat, don't try to fool me! I will gut yer insides!"
        )


if __name__ == "__main__":
    main(sys.argv[1:])

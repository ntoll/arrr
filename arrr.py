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
import random
import sys


#: The help text to be shown when requested.
_HELP_TEXT = """
Take English words and turn them into something Pirate-ish.

Documentation here: https://arrr.readthedocs.io/en/latest/
"""


#: MAJOR, MINOR, RELEASE, STATUS [alpha, beta, final], VERSION
_VERSION = (1, 0, 2)


#: Defines English to Pirate-ish word substitutions.
_PIRATE_WORDS = {
    "hello": "ahoy",
    "hi": "arrr",
    "my": "me",
    "friend": "m'hearty",
    "boy": "laddy",
    "girl": "lassie",
    "sir": "matey",
    "miss": "proud beauty",
    "stranger": "scurvy dog",
    "boss": "foul blaggart",
    "where": "whar",
    "is": "be",
    "the": "th'",
    "you": "ye",
    "old": "barnacle covered",
    "happy": "grog-filled",
    "nearby": "broadside",
    "bathroom": "head",
    "kitchen": "galley",
    "pub": "fleabag inn",
    "stop": "avast",
    "yes": "aye",
    "no": "nay",
    "yay": "yo-ho-ho",
    "money": "doubloons",
    "treasure": "booty",
    "strong": "heave-ho",
    "take": "pillage",
    "drink": "grog",
    "idiot": "scallywag",
    "sea": "briney deep",
    "vote": "mutiny",
    "song": "shanty",
    "drunk": "three sheets to the wind",
    "lol": "yo ho ho",
    "talk": "parley",
    "fail": "scupper",
    "quickly": "smartly",
    "captain": "cap'n",
}


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
    # Normalise a list of words (remove whitespace and make lowercase)
    words = [w.lower() for w in english.split()]
    # Substitute some English words with Pirate equivalents.
    result = [_PIRATE_WORDS.get(word, word) for word in words]
    # Capitalize words that begin a sentence and potentially insert a pirate
    # phrase with a chance of 1 in 5.
    capitalize = True
    for i, word in enumerate(result):
        if capitalize:
            result[i] = word.capitalize()
            capitalize = False
        if word.endswith((".", "!", "?", ":",)):
            # It's a word that ends with a sentence ending character.
            capitalize = True
            if random.randint(0, 5) == 0:
                result.insert(i + 1, random.choice(_PIRATE_PHRASES))
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


if __name__ == "__main__":
    main(sys.argv[1:])

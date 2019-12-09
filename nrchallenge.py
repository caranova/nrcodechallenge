import os
import sys
import argparse
import fileinput
from collections import Counter
import regex


def showtally(func):
    def wrapper(*args, **kwargs):
        for [phrase, tally] in func(*args, **kwargs):
            print(phrase + " - " + str(tally))
    return wrapper


@showtally
def tally_three_word_phrase(text: str, num=100):
    """Tally the occurances of three-word phrases in given text.

    Keyword Arguments:
    text -- the text to be searched for three-word phrases
    num  -- the number of results to keep (default 100)
    """
    match = regex.findall(r'(?=\b(\w+ +\w+ +\w+)\b)', text)
    count = Counter()
    count.update([phrase for phrase in match])
    return count.most_common()[:num]


parser = argparse.ArgumentParser(
    description=("When given text(s) will return a list of the \n"
                 "100 most common three word sequences.")
)

parser.add_argument(
    "--file",
    "-f",
    type=argparse.FileType('r', encoding='utf-8'),
    nargs='+',
    help='input file(s) for script, if none assume stdin-only',
    default=sys.stdin)

args = parser.parse_args()

if (not args.file):
    sys.exit("pipe via stdin or pass file(s)")

fulltext = ''  # to hold the lower-case full  (concatenated) text files

if type(args.file) is list:
    # concatenate any number of files so that phrase
    # matches are assessed from the whole, not just the parts,
    # and make them lower-case so that the search is case-insensitive
    for f in args.file:
        fulltext += f.read().lower()
else:
    fulltext = args.file.read().lower()

tally_three_word_phrase(fulltext)

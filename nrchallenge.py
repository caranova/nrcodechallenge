import os, sys, regex, argparse, fileinput
from collections import Counter


parser = argparse.ArgumentParser(
    description="When given text(s) will return a list of the \n100 most common three word sequences."
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

lower_text = '' # to hold the lower-case text
if type(args.file) is list:
    for f in args.file:
        lower_text += f.read().lower() # concatenate both files so that matches match from the whole,
                                       # not just the parts, and make them lower-case so that the search is case insensitive
else:
    lower_text = args.file.read().lower() # this gets the piped file input, since it isnt parsed as a file-list

m = regex.findall(r'(?=\b(\w+ +\w+ +\w+)\b)',lower_text) # matches 3 words including any number of spaces 
                                                         # between them and captures the three word sequence as a capture group
c = Counter() # dict subclass

for threeword in m: # for each three-word 'phrase' in the match , add a tally
    c[threeword] +=1
mostcommon = c.most_common()[:100] #sort them by most common and truncate to the first 100

for [phrase,tally] in mostcommon:
    print(phrase + " - " + str(tally))


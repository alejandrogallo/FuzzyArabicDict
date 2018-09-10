# Explore using a pickled file rather than redis

import six.moves.cPickle as pickle
from collections import defaultdict
from aramorph.aramorpher import Morpheme, Aramorpher
from aramorph.process_files import process_textfile, process_tableXY
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')

def process_prefixes():
    prefixes = defaultdict(list)
    path = os.path.join(data_dir, 'dictprefixes.txt')
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(path):
        prefixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return prefixes

def process_stems():
    stems = defaultdict(list)
    path = os.path.join(data_dir, 'dictstems.txt')
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(path):
        stems[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return stems

def process_suffixes():
    suffixes = defaultdict(list)
    path = os.path.join(data_dir, 'dictsuffixes.txt')
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(path):
        suffixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return suffixes

def process_tableAB():
    ab = defaultdict(list)
    path = os.path.join(data_dir, 'tableab.txt')
    for (left, right) in process_tableXY(path):
        ab[left].append(right)
    return ab

def process_tableBC():
    bc = defaultdict(list)
    path = os.path.join(data_dir, 'tablebc.txt')
    for (left, right) in process_tableXY(path):
        bc[left].append(right)
    return bc

def process_tableAC():
    ac = defaultdict(list)
    path = os.path.join(data_dir, 'tableac.txt')
    for (left, right) in process_tableXY(path):
        ac[left].append(right)
    return ac

def get_aramorpher():
    prefixes = process_prefixes()
    stems = process_stems()
    suffixes = process_suffixes()
    ab = process_tableAB()
    bc = process_tableBC()
    ac = process_tableAC()

    return Aramorpher(prefixes, stems, suffixes, ab, bc, ac)

if __name__ == "__main__":

    morph = get_aramorpher()

    # and pickle it
    data_file = os.path.join(current_dir, 'aramortph.data')
    pickle.dump(morph, open(data_file, "wb+"), pickle.HIGHEST_PROTOCOL)

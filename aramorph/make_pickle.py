import six.moves.cPickle as pickle
from collections import defaultdict
from aramorph.aramorpher import Morpheme, Aramorpher
from aramorph.process_files import process_textfile, process_tableXY
from aramorph.data import (
    prefixes_path,
    stems_path,
    suffixes_path,
    tableab_path,
    tablebc_path,
    tableac_path,
    aramorph_path
)


def process_prefixes():
    prefixes = defaultdict(list)
    p = prefixes_path
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(p):
        prefixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return prefixes


def process_stems():
    stems = defaultdict(list)
    p = stems_path
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(p):
        stems[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return stems


def process_suffixes():
    suffixes = defaultdict(list)
    p = suffixes_path
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(p):
        suffixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return suffixes


def process_tableAB():
    ab = defaultdict(list)
    for (left, right) in process_tableXY(tableab_path):
        ab[left].append(right)
    return ab


def process_tableBC():
    bc = defaultdict(list)
    for (left, right) in process_tableXY(tablebc_path):
        bc[left].append(right)
    return bc


def process_tableAC():
    ac = defaultdict(list)
    for (left, right) in process_tableXY(tableac_path):
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

    with open(aramorph_path, "wb+") as f:
        pickle.dump(morph, f, pickle.HIGHEST_PROTOCOL)

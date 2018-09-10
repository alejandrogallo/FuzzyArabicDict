import six.moves.cPickle as pickle
from collections import defaultdict
from aramorph.aramorpher import Morpheme, Aramorpher
from aramorph.parsers import parse_textfile, parse_tableXY
from aramorph.data import (
    prefixes_path,
    stems_path,
    suffixes_path,
    tableab_path,
    tablebc_path,
    tableac_path,
    aramorph_path
)


def parse_prefixes():
    prefixes = defaultdict(list)
    p = prefixes_path
    for (unvowelled, vowelled, cat, pos, gloss, root) in parse_textfile(p):
        prefixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return prefixes


def parse_stems():
    stems = defaultdict(list)
    p = stems_path
    for (unvowelled, vowelled, cat, pos, gloss, root) in parse_textfile(p):
        stems[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return stems


def parse_suffixes():
    suffixes = defaultdict(list)
    p = suffixes_path
    for (unvowelled, vowelled, cat, pos, gloss, root) in parse_textfile(p):
        suffixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))
    return suffixes


def parse_tableAB():
    ab = defaultdict(list)
    for (left, right) in parse_tableXY(tableab_path):
        ab[left].append(right)
    return ab


def parse_tableBC():
    bc = defaultdict(list)
    for (left, right) in parse_tableXY(tablebc_path):
        bc[left].append(right)
    return bc


def parse_tableAC():
    ac = defaultdict(list)
    for (left, right) in parse_tableXY(tableac_path):
        ac[left].append(right)
    return ac


def get_aramorpher():
    # TODO: get pickle to work
    #with open(aramorph.data.aramorph_path, "rb") as f:
        #ai = load(f)
    prefixes = parse_prefixes()
    stems = parse_stems()
    suffixes = parse_suffixes()
    ab = parse_tableAB()
    bc = parse_tableBC()
    ac = parse_tableAC()
    return Aramorpher(prefixes, stems, suffixes, ab, bc, ac)


def create_pickle_aramorpher_file():
    morph = get_aramorpher()
    with open(aramorph_path, "wb+") as f:
        pickle.dump(morph, f, pickle.HIGHEST_PROTOCOL)

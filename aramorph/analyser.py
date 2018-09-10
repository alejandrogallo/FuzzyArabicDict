"""
This loads the pickled Aramorpher object, making it available to do analysis

Run this first:
> python make_pickle.py
"""

from six.moves.cPickle import load

import sys
import aramorph.data

# this is a hacky (?) way of getting the pickled object in a subdirectory
# to load properly when called from an upper-level directory
import aramorph.aramorpher as aramorpher
sys.modules['aramorpher'] = aramorpher

with open(aramorph.data.aramorph_path, "rb") as f:
    ai = load(f)

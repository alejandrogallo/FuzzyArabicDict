"""
This loads the pickled Aramorpher object, making it available to do analysis

Run this first:
> python make_pickle.py
"""

from six.moves.cPickle import load

import os
import sys

# this is a hacky (?) way of getting the pickled object in a subdirectory
# to load properly when called from an upper-level directory
import aramorph.aramorpher as aramorpher
sys.modules['aramorpher'] = aramorpher

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'aramorph.data')
with open(data_path, "rb") as f:
    ai = load(f)

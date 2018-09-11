from aramorph.data import *

def test_vars():
    assert(os.path.exists(data_dir))
    assert(os.path.exists(prefixes_path))
    assert(os.path.exists(stems_path))
    assert(os.path.exists(suffixes_path))
    assert(os.path.exists(tableab_path))
    assert(os.path.exists(tablebc_path))
    assert(os.path.exists(tableac_path))
    assert(aramorph_path is not None)

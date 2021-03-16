import bz2
import _pickle as cPkl

def dump_cPkl(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f: 
        cPkl.dump(data, f)

def load_cPkl(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPkl.load(data)
    return data
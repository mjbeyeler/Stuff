import gzip as gz
import _pickle as cPkl

def dump_cPkl(title, data):
    with gz.open(title + '.pgz', 'wb') as f: 
        cPkl.dump(data, f, protocol=-1)

def load_cPkl(file):
    with gz.open(file, 'rb') as f: 
        data = cPkl.load(f)
        return data
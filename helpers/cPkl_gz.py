import gzip as gz
import _pickle as cPkl

def dump(title, data):
    with gz.open(title + '.pgz', 'wb') as f: 
        cPkl.dump(data, f, protocol=-1)

def load(file):
    with gz.open(file, 'rb') as f: 
        data = cPkl.load(f)
        return data
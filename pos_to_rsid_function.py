from PascalX import genescorer
from PascalX import snpdb
import pandas as pd
import numpy as np

def pos_to_rsid(positions):


    Scorer = genescorer.chi2sum()
    Scorer.load_refpanel("/SSD/home/michael/retina_tortuosity/data/reference_panels/UK10K_hg19/TWINSUK.and.ALSPAC", parallel=10)

    out = pd.Series([np.nan for i in range(0,len(positions))])

    for i in range(1,23):
        lst_gen = [(k,int(j.split(":")[1])) for k,j in enumerate(positions) if int(j.split(":")[0])==i]
        idx = [j[0] for j in lst_gen]
        pos = [j[1] for j in lst_gen]
        my_chr,mylist=Scorer._ref.load_pos_reference(str(i))
        rsids=my_chr.get(pos)
        
        #print(idx[0:10])
        #print(pos[0:10])
        #print(rsids[0:10])

        # removing SNPs not present in the refpanel
        lst_gen = [(k,j[0]) for (k,j) in enumerate(rsids) if j is not None]
        idx_idx = [j[0] for j in lst_gen]
        rsids = [j[1] for j in lst_gen]
        
        #print(rsids)

        #print(len(idx))
        idx = np.array(idx)
        idx = idx[idx_idx]
        #print(len(idx))
        
        out[idx] = rsids

    return out.to_list()
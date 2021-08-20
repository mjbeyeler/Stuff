# Author: mjbeyeler
# Summary: PascalX-based conversion of genome position information to rsIDs
# At the moment works with a specific dataframe, can convert into simple function to
# inputting and outputting list

from PascalX import genescorer
import config
Scorer = genescorer.chi2sum(varcutoff=config.VARCUTOFF, window=config.WINDOW)
Scorer.load_refpanel(config.REFERENCE_PANEL, parallel=config.N_CORES)

from PascalX import snpdb

import pandas as pd
import numpy as np

df = pd.read_csv("~/code/out_skipogh_colaus_metaanalysis.csv")
df['rsid'] = np.nan

for i in range(1,23):
    lst_gen = [(k,int(j.split(":")[1])) for k,j in enumerate(df["SNP"]) if int(j.split(":")[0])==i]
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
    
    df.loc[idx, 'rsid'] = rsids


df.to_csv("~/code/out_skipogh_colaus_metaanalysis_with_rsIDs.csv")

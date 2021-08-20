import pandas as pd
import numpy as np
from scipy import stats

df=pd.read_csv("~/data/metaanalysis_colaus_skipogh_RE2C.txt", delimiter=" ", names=['SNP','beta1', 'se1', 'beta2', 'se2'])
df['CHR'] = [i.split(":")[0] for i in df['SNP']]
df['BP'] = [i.split(":")[1] for i in df['SNP']]
df['weight1'] = 1/df['se1']**2
df['weight2'] = 1/df['se2']**2
df['beta_meta'] = (df['beta1'] * df['weight1'] + df['beta2'] * df['weight2']) / (df['weight1'] + df['weight2'])
df['se_meta'] = np.sqrt(1/(df['weight1']+df['weight2']))
df['t_meta'] = df['beta_meta']/df['se_meta']
df['P'] = stats.t.sf(np.abs(df['t_meta']), 397+514-1)*2 # two-sided t-test with cohortSize-1 degrees of freedom
df[['SNP', 'beta1', 'se1', 'beta2', 'se2', 'weight1','weight2', 'beta_meta', 'se_meta', 't_meta', 'P', 'CHR', 'BP']].to_csv("out_skipogh_colaus_metaanalysis.csv",index=False)

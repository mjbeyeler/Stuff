#%%
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from matplotlib import cm
import csv

input_dir = "../fdfad"
output_dir = "../imageStatsDF/"

for i in os.listdir():
    if i.endswith("segmentStats.tsv"):
        # loading image-specific segment stats:
        df = pd.read_csv(i, delimiter='\t')

        imageID = i.split("_all_segmentStats")[0]


        segLen_quints = np.quantile(df["arcLength"], [0.2,0.4,0.6,0.8])
        segLen_q1Inds = df["arcLength"].loc[df["arcLength"] < segLen_quints[0]].index
        segLen_q2Inds = df["arcLength"].loc[(df["arcLength"] < segLen_quints[1]) \
            & (df["arcLength"] >= segLen_quints[0])].index
        segLen_q3Inds = df["arcLength"].loc[(df["arcLength"] < segLen_quints[2]) \
            & (df["arcLength"] >= segLen_quints[1])].index
        segLen_q4Inds = df["arcLength"].loc[(df["arcLength"] < segLen_quints[3]) \
            & (df["arcLength"] >= segLen_quints[2])].index
        segLen_q5Inds = df["arcLength"].loc[df["arcLength"] >= segLen_quints[3]].index


        with open(output_dir + imageID + "_all_imageStats.tsv", 'w') as f:
            f.write("DF1st\tDF2nd\tDF3rd\tDF4th\tDF5th\n")

            f.write("%s\t" % np.median(df['DF'].iloc[segLen_q1Inds]))
            f.write("%s\t" % np.median(df['DF'].iloc[segLen_q2Inds]))
            f.write("%s\t" % np.median(df['DF'].iloc[segLen_q3Inds]))
            f.write("%s\t" % np.median(df['DF'].iloc[segLen_q4Inds]))
            f.write("%s\t" % np.median(df['DF'].iloc[segLen_q5Inds]))
# %%

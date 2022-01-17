import pandas as pd
df1 = pd.read_csv("/SSD/home/michael/retina_tortuosity/output/GWAS_all/skipogh_DF_GWAS_Tanguy/SKIPOGH_retina_median_tortuosity_QQ.epacts", delimiter='\t')
df1['MARKER_ID'] = [i.split("_")[0] for i in df1['MARKER_ID']]

df2=pd.read_csv("/SSD/home/michael/retina_tortuosity/output/GWAS_all/2021_07_19_ophthalmolausRawMeasurements_withPCs/output_CoLaus.HRC.all.txt", delimiter=" ")
df2 = df2[["rsid","DF_beta","DF_se"]]

df2 = df2.dropna()
df1 = df1.dropna()

df1 = df1.set_index("MARKER_ID")
df2 = df2.set_index("rsid")

joint_snps = set(df1.index) & set(df2.index)

df_meta = df1[["BETA","SEBETA"]].loc[joint_snps]
df_meta[["COLAUS_BETA","COLAUS_SEBETA"]]=df2[["DF_beta","DF_se"]].loc[joint_snps]

df_meta.to_csv("~/data/metaanalysis_colaus_skipogh_RE2C.txt", sep=" ", header=False)

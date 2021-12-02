import pandas as pd

df = pd.read_csv("ALL.counts", sep="\t")

df.rename(columns={"0": "geneID"}, inplace=True)
df = df[["geneID", "c1", "c2", "c3", "r1", "r2", "r3"]]

df.to_csv("improved_ALL.counts", sep="\t", index=False)

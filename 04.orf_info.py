import pandas as pd
import csv

# read file
data = pd.read_csv('ribotricer_index_GRCh38.110.chr_gtf_30nt_all_candidate_orfs.tsv', sep='\t', header=None)
# remove header
data = data.iloc[1:]

# select column
selected_columns = data.iloc[:, [0, 2]]

orf_ids = []
for index, row in selected_columns.iterrows():
    orf_id = row[0].split("_")
    gstart = int(float(orf_id[1]))
    gend = int(float(orf_id[2]))
    orig_id = row[0]
    enst_id = row[2]
    orf_ids.append((orig_id, enst_id, gstart, gend))

# write file
with open("targ_f.tsv", "w") as f:
    writer = csv.writer(f, delimiter="\t")
    for orf_id in orf_ids:
        writer.writerow(orf_id)

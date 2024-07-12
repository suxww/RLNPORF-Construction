# input tsv and bed path
tsv_file = "ribotricer_index_GRCh38.103.chr_gtf_all_candidate_orfs.tsv" 
bed_file = "sorf_coord.bed"       

# write file
with open(bed_file, 'w') as output_bed:
    with open(tsv_file, 'r') as input_tsv:
        #each line
        for line in input_tsv:
            # Skip the header line
            if line.startswith("ORF_ID"):
                continue
            
            # each field
            fields = line.strip().split("\t")
            chrom = fields[7]
            orf_id = fields[0]
            coordinates = fields[-1].split(",")
            
            # Extract each coordinate segment 
            for coordinate in coordinates:
                start, end = coordinate.split("-")
                start = int(start)-1
                end = int(end)
                
                # write BED file
                bed_line = f"{chrom}\t{start}\t{end}\t{orf_id}\t.\t{fields[8]}\n"
                output_bed.write(bed_line)
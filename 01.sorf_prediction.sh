#!/bin/bash

ribotricer prepare-orfs \
        --gtf ~/data/reference/ensembl/Homo_sapiens.GRCh38.103.chr.gtf \
        --fasta ~/data/reference/ensembl/Homo_sapiens.GRCh38.dna_103.primary_assembly.fa \
        --prefix ~/sORF_ribotricer/ens110/ribotricer_index_GRCh38.103.chr_gtf_30nt_all \
        --start_codons ATG,CTG,GTG,TTG 
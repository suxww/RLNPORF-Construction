from collections import defaultdict

# input and output file path
fasta_file = "sorf_scoord.fa"   
output_fasta = "sorf_test.fa"     

# Create a defaultdict to store sequences with the same ID prefix
sequences = defaultdict(str)

with open(fasta_file, 'r') as input_fasta:
    current_id = ""
    current_sequence = ""
    # each line
    for line in input_fasta:
        line = line.strip()
        # update sequence
        if line.startswith(">"):
            # If not empty, store in the sequences dictionary
            if current_id:
                sequences[current_id] += current_sequence.upper()  # change upper
            current_id = line.split("::")[0][1:]
            current_sequence = ""
        else:
            current_sequence += line
    
    # store last one
    if current_id:
        sequences[current_id] += current_sequence.upper()  # change upper


with open(output_fasta, 'w') as output_file:
    for seq_id, sequence in sequences.items():
        output_file.write(f">{seq_id}\n{sequence}\n")
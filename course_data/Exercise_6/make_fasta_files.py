# Python script to make 10 DNA FASTA files in which one has a higher GC content than
# the others

import random
import gzip

seq_length = 10_000
random_seed = 42

# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Functions
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
def random_dna_with_gc(length, gc_fraction):
    """
    Generate a random DNA sequence with a specified GC content.

    Parameters:
        length (int): Length of the DNA sequence.
        gc_fraction (float): Desired GC content (0 to 1).

    Returns:
        str: Random DNA sequence.
    """
    if not (0 <= gc_fraction <= 1):
        raise ValueError("gc_fraction must be between 0 and 1.")
    
    # Number of G/C bases to include
    gc_count = int(length * gc_fraction)
    at_count = length - gc_count

    # Create GC and AT pools
    gc_bases = random.choices(["G", "C"], k=gc_count)
    at_bases = random.choices(["A", "T"], k=at_count)

    # Combine and shuffle
    seq_list = gc_bases + at_bases
    random.shuffle(seq_list)

    return "".join(seq_list)


# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Main script
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

random.seed(random_seed)
ecoli_sample_number = random.choice(range(1, 11))

print('Generating DNA FASTA files')
for i in range(1, 11):

    random.seed(i)   # Varies sequence between samples, but the same each time script executed
    outfile = f'sample.{i}.fa.gz'

    if i == ecoli_sample_number:
        sample_gc = 0.51
    else:
        sample_gc = 0.41 + ( random.choice(range(-5, 5)) / 100) # Create some variability

    with gzip.open(outfile, 'wb') as f_out:
        header = f'>{i}\n'
        f_out.write(header.encode('utf-8'))
        
        seq = random_dna_with_gc(seq_length, sample_gc)
        seq = f'{seq}\n'
        f_out.write(seq.encode('utf-8'))
    
print('Done')
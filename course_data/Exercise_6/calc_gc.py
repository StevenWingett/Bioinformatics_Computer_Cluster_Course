# This script reports the GC content of a DNA FASTA file

import gzip
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument("fasta_file", action="store", type=str, metavar='',
                    help="Path to FASTA file to calculate GC")


args = parser.parse_known_args()    #Use parse_known_arg to differentiate between arguments pre-specified and those that are not
options = args[0]   # Get the 2 arrays of known/unknown arguments from the tuple


# # # # # # # # # # # # # # # # # # # # # # 
# Functions
# # # # # # # # # # # # # # # # # # # # # # 

def smart_open(filename, mode='rt'):
    """
    Open a file normally or with gzip based on file extension.

    Parameters:
        filename (str): path to the file
        mode (str): file mode ('rt' for text, 'rb' for binary)
    """
    if filename.endswith('.gz'):
        return gzip.open(filename, mode)
    else:
        return open(filename, mode)


def gc_content(sequence: str) -> float:
    """Calculate GC content (%) of a DNA sequence."""
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100 if sequence else 0



# # # # # # # # # # # # # # # # # # # # # # 
# Main script
# # # # # # # # # # # # # # # # # # # # # # 

print("Processing " + options.fasta_file)
time.sleep(100)  # Deliberate delay so the job's progress may be observed with squeue

seq = ''
with smart_open(options.fasta_file) as f_in:
    for line in f_in:
        if line[0] == '>':
            continue
        else:
            seq += line.strip()

print(gc_content(seq))

print('Done')

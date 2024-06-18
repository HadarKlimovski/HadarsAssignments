import sys
import argparse
from Bio import SeqIO

def find_longest_duplicate_subsequence(sequence):
    n = len(sequence)
    longest_dup = ""
    
    for i in range(n):
        for j in range(i + 1, n):
            lcs_temp = 0
            
            while j + lcs_temp < n and sequence[i + lcs_temp] == sequence[j + lcs_temp]:
                lcs_temp += 1
            
            if lcs_temp > len(longest_dup):
                longest_dup = sequence[i:i + lcs_temp]
    
    return longest_dup

def find_longest_gc_sequence(sequence):
    max_length = 0
    max_seq = ""
    current_length = 0
    current_seq = ""

    for base in sequence:
        if base in "GCgc":
            current_length += 1
            current_seq += base
        else:
            if current_length > max_length:
                max_length = current_length
                max_seq = current_seq
            current_length = 0
            current_seq = ""
    
    # Check the last sequence if it was the longest
    if current_length > max_length:
        max_length = current_length
        max_seq = current_seq

    return max_seq

def main():
    parser = argparse.ArgumentParser(description='Sequence Analysis Tool')
    parser.add_argument('file', help='Path to the input file (FASTA or GeneBank format)')
    parser.add_argument('--duplicate', action='store_true', help='Find the longest duplicate sub-sequence')
    parser.add_argument('--cg_long', action='store_true', help='Find the longest GC combination sequence')

    args = parser.parse_args()

    # Read the sequence from the file
    sequence = ""
    for record in SeqIO.parse(args.file, "fasta"):
        sequence += str(record.seq)
    
    # Perform analyses based on the command-line arguments
    if args.duplicate:
        longest_dup = find_longest_duplicate_subsequence(sequence)
        print(f"Longest duplicate sub-sequence: {longest_dup}")
    
    if args.cg_long:
        longest_gc_seq = find_longest_gc_sequence(sequence)
        print(f"Longest GC combination sequence: {longest_gc_seq}")

if __name__ == '__main__':
    main()


# Sequence Analysis Tool

This Python program provides tools for analyzing DNA sequences from FASTA or GeneBank format files. It includes functionality to find the longest duplicate sub-sequence and the longest contiguous GC combination sequence within a DNA sequence.

## Features


1. **Find Longest Duplicate Sub-sequence**: Identifies the longest sub-sequence that appears twice in the given DNA sequence

    ```bash
    python analyze.py sequence.fasta --duplicate
    ```

2. **Find Longest GC Combination Sequence**: Identifies the longest contiguous sequence of 'G' and 'C' nucleotides:

    ```bash
    python analyze.py sequence.fasta --cg_long
    ```

## File Structure

- `analyze.py`: The main script that performs the sequence analyses.
- `sequence.fasta`:input file in FASTA format[hemoglibine beta in thos case].

## Installation:
Install the required packages using pip:

```
pip install -r requirements.txt
```


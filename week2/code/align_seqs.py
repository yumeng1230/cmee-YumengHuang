#!/usr/bin/env python3

import os
"""
This script reads two DNA sequences from a file, aligns them to find the best match,
and writes the alignment result to an output file.

Functions:
    - read_sequences_from_file: Reads two sequences from an input file.
    - calculate_score: Computes the alignment score for two sequences.
    - align_sequences: Finds the best alignment for two sequences.
    - write_results: Writes the best alignment and its score to an output file.

Usage:
    python3 align_seqs.py

Input:
    - ../data/seqs_data.csv: A file containing two DNA sequences in the format:
        seq1="CAATTCGGAT"
        seq2="ATCGCCGGATTACGGG"

Output:
    - ../results/alignment_results.txt: A file containing:
        - The best alignment string.
        - The longer sequence.
        - The highest alignment score.
"""


def read_sequences_from_file(file_path):
    """
    Reads sequences from a file and returns seq1 and seq2.

    Args:
        file_path (str): Path to the input file containing sequences.

    Returns:
        tuple: A tuple (seq1, seq2) containing the sequences, or (None, None) if an error occurs.
    """
    sequences = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue

                # Parse lines like seq1="CAATTCGGAT"
                try:
                    key, value = line.split('=')
                    sequences[key.strip()] = value.strip().strip('"')  # Remove spaces and quotes
                except ValueError as e:
                    print(f"Error parsing line: {line.strip()}, Error message: {e}")
                    continue

        return sequences.get('seq1'), sequences.get('seq2')
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return None, None


def calculate_score(s1, s2, l1, l2, startpoint):
    """
    Computes the alignment score for two sequences starting from a given startpoint.

    Args:
        s1 (str): The longer sequence.
        s2 (str): The shorter sequence.
        l1 (int): Length of the longer sequence.
        l2 (int): Length of the shorter sequence.
        startpoint (int): Starting point for alignment.

    Returns:
        int: The alignment score.
    """
    matched = ""  # To hold string displaying alignments
    score = 0

    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]:  # If the bases match
                matched += "*"
                score += 1
            else:
                matched += "-"

    # Output alignment results
    print("." * startpoint + matched)
    print("." * startpoint + s2)
    print(s1)
    print(f"Score: {score}")
    print(" ")

    return score


def align_sequences(seq1, seq2):
    """
    Aligns two sequences and finds the best alignment with the highest score.

    Args:
        seq1 (str): The first sequence.
        seq2 (str): The second sequence.

    Returns:
        tuple: A tuple (best_align, best_score), where best_align is the alignment string,
               and best_score is the highest score.
    """
    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1, s2 = seq1, seq2
    else:
        s1, s2 = seq2, seq1
        l1, l2 = l2, l1  # Swap lengths

    best_align = None
    best_score = -1

    for i in range(l1):
        score = calculate_score(s1, s2, l1, l2, i)
        if score > best_score:
            best_align = "." * i + s2
            best_score = score

    return best_align, best_score


def write_results(output_path, best_align, s1, best_score):
    """
    Writes the alignment results to a file.

    Args:
        output_path (str): Path to the output file.
        best_align (str): The best alignment string.
        s1 (str): The longer sequence.
        best_score (int): The highest alignment score.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        f.write(f"{best_align}\n")
        f.write(f"{s1}\n")
        f.write(f"Best score: {best_score}\n")

    print(f"Results have been written to {output_path}")


if __name__ == "__main__":
    input_file = "../data/seqs_data.csv"
    output_file = "../results/alignment_results.txt"

    seq1, seq2 = read_sequences_from_file(input_file)

    if seq1 and seq2:
        print(f"Seq1: {seq1}")
        print(f"Seq2: {seq2}")

        best_align, best_score = align_sequences(seq1, seq2)
        write_results(output_file, best_align, seq1, best_score)
    else:
        print("Failed to read sequences. Please check the input file.")

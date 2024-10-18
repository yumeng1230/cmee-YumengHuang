# Two example sequences to match
# seq2 = "ATCGCCGGATTACGGG"
# seq1 = "CAATTCGGAT"

# Assign the longer sequence to s1, and the shorter to s2
# l1 is the length of the longest, l2 that of the shortest

# Function to read sequences from a file
def read_sequences_from_file(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        for line in file:
            print(f"Read line: {line.strip()}")  # Print each line for debugging

            # Skip empty lines
            if line.strip() == "":
                continue

            # Parse lines like seq1="CAATTCGGAT"
            try:
                key, value = line.split('=')  # Separate seq1="CAATTCGGAT"
                sequences[key.strip()] = value.strip().strip('"')  # Remove spaces and quotes
            except Exception as e:
                print(f"Error parsing line: {line}, Error message: {e}")
                continue

    return sequences.get('seq1'), sequences.get('seq2')

# Specify input file
input_file = "../data/seqs_data.csv"  
seq1, seq2 = read_sequences_from_file(input_file)

# Check if both sequences were successfully read
if seq1 and seq2:
    print(f"Seq1: {seq1}")
    print(f"Seq2: {seq2}")
else:
    print("Failed to read Seq1 or Seq2")

# Example: Call the function
input_file = "../data/seqs_data.csv"  # Specify file path
seq1, seq2 = read_sequences_from_file(input_file)
print(f"Seq1: {seq1}")
print(f"Seq2: {seq2}")

# Determine which sequence is longer
l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1  # Swap the two lengths

# A function that computes a score by returning the number of matches
# starting from an arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    matched = ""  # To hold string displaying alignments
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]:  # If the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # Some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# Now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1):  # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2  # Think about what this is doing!
        my_best_score = z  

import os

# Ensure ../results directory exists, create it if not
if not os.path.exists('../results'):
    os.makedirs('../results')

# Open ../results/alignment_results.txt file and write the results
with open('../results/alignment_results.txt', 'w') as f:
    # Output my_best_align, s1, and my_best_score to the file
    print(my_best_align, file=f)
    print(s1, file=f)
    print(f"Best score: {my_best_score}", file=f)

print("Results have been written to ../results/alignment_results.txt")

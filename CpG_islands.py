import math
from collections import Counter

def read_fasta(file_path):
    """Reads a FASTA file and returns the sequence."""
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

def calculate_dinucleotide_frequencies(sequence):
    """Calculates the frequency of each dinucleotide in the sequence."""
    total = len(sequence) - 1
    dinucleotides = [sequence[i:i+2] for i in range(len(sequence) - 1)]
    frequencies = Counter(dinucleotides)
    for dinucleotide in frequencies:
        frequencies[dinucleotide] /= total
    return frequencies

 ################################################################
 #similar to CpG_frequency.py



def calculate_markov_model(sequence, dinucleotide_freq):
    """Calculates a Markov model based on dinucleotide frequencies."""
    model = {nucleotide: {} for nucleotide in 'ACGT'}
    for dinucleotide in dinucleotide_freq:
        n1, n2 = dinucleotide
        model[n1][n2] = dinucleotide_freq[dinucleotide]
    return model


def calculate_probability(markov_model, substring):
    """Calculates the probability of a substring based on a Markov model."""
    if not substring:
        return 0

    probability = 1.0
    for i in range(len(substring) - 1):
        n1, n2 = substring[i], substring[i + 1]
        probability *= markov_model[n1].get(n2, 0)

    return probability

def cpg_potential_score(cpg_model, non_cpg_model, substring):
    """Calculates the CpG potential score for a substring."""
    probability_cpg = calculate_probability(cpg_model, substring)
    probability_non_cpg = calculate_probability(non_cpg_model, substring)

    if probability_non_cpg == 0:
        return float('inf') if probability_cpg > 0 else float('-inf')

    return math.log(probability_cpg / probability_non_cpg)

# Load the FASTA file and calculate dinucleotide frequencies
fasta_file = 'chrA.fasta'
sequence = read_fasta(fasta_file)
dinucleotide_freq = calculate_dinucleotide_frequencies(sequence)

# Assume non_cpg_dinucleotide_freq is available or calculated similarly
non_cpg_dinucleotide_freq = {}  # Replace with actual frequencies

# Calculate Markov models
cpg_markov_model = calculate_markov_model(sequence, dinucleotide_freq)
non_cpg_markov_model = calculate_markov_model(sequence, non_cpg_dinucleotide_freq)

# Predict CpG islands and compare with chrA.islands
# Load chrA.islands data
island_locations = []  # Load the actual island locations

# Iterate over the sequence and calculate CpG potential scores
predictions = []
for start in range(len(sequence)-200):
    for end in range(start+200,len(sequence)):
        substring = sequence[start:end]
        score = cpg_potential_score(cpg_markov_model, non_cpg_markov_model, substring)
        if score > 0:  # Positive score indicates CpG island
            predictions.append((start, end))

# Compare predictions with actual locations and calculate statistics
true_positive = false_positive = false_negative = 0
for prediction in predictions:
    if prediction in island_locations:
        true_positive += 1
    else:
        false_positive += 1

for location in island_locations:
    if location not in predictions:
        false_negative += 1


with open("CpG_islands", "w") as f:
    line = f"True Positive: {true_positive}, False Positive: {false_positive}, False Negative: {false_negative}"
    f.write(line)



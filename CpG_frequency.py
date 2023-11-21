from collections import Counter

def read_fasta(file_path):
    """Reads a FASTA file and returns the sequence."""
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

def calculate_nucleotide_frequencies(sequence):
    """Calculates the frequency of each nucleotide in the sequence."""
    total = len(sequence)
    frequencies = Counter(sequence)
    for nucleotide in frequencies:
        frequencies[nucleotide] /= total
    return frequencies

def calculate_dinucleotide_frequencies(sequence):
    """Calculates the frequency of each dinucleotide in the sequence."""
    total = len(sequence) - 1
    dinucleotides = [sequence[i:i+2] for i in range(len(sequence) - 1)]
    frequencies = Counter(dinucleotides)
    for dinucleotide in frequencies:
        frequencies[dinucleotide] /= total
    return frequencies

def CpG_frequencies(sequence):
    """Compares observed and expected dinucleotide frequencies."""
    nucleotide_freq = calculate_nucleotide_frequencies(sequence)
    dinucleotide_observed = calculate_dinucleotide_frequencies(sequence)

    dinucleotide_expected = {}
    for dinucleotide in dinucleotide_observed:
        n1, n2 = dinucleotide
        dinucleotide_expected[dinucleotide] = nucleotide_freq[n1] * nucleotide_freq[n2]

    significant_differences = {}
    for dinucleotide in dinucleotide_observed:
        observed = dinucleotide_observed[dinucleotide]
        expected = dinucleotide_expected[dinucleotide]
        if abs(observed - expected) > 0.01:  # Threshold for significance
            significant_differences[dinucleotide] = (observed, expected)

    return significant_differences

fasta_file = 'chrA.fasta'
sequence = read_fasta(fasta_file)
significant_differences = CpG_frequencies(sequence)

with open("CpG_frequency_return.txt", "w") as file:
    for dinucleotide, (observed, expected) in significant_differences.items():
        line = f"{dinucleotide}: {observed},{expected}\n"
        file.write(line)

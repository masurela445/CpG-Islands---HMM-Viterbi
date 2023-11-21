# CpG-Islands---HMM-Viterbi
chrA.fasta: DNA sequence for which the locations of the CpG islands are known
chrA.islands: locations (start & end) of the CpG islands in chrA.fasta

CpG_frequency.py: calculate the frequency of each dinucleotide.
Compare the observed frequency of each dinucleotide to its expected frequency (based on the frequencies
of A, C, G and T nucleotides)
Input: chrA.fasta
Output: CpG_frequency_return.txt

CpG_islands.py: 
Input: chrA.fasta
Output: chrA.islands
Utilizing the dinucleotide frequencies from CpG_frequency.py, this program implement a first-order Markov model with four states (one for each nucleotide) where the transition probabilities correspond to the dinucleotide frequencies. Similarly, it implement a first-order Markov model for sequence outside CpG
islands. It takes as input a string S, begin and end coordinates (b, e) of a substring
on S, and compute the CpG potential score:
CpG potential = log (PrCpG S[b, e]/Prnon-CpG S[b, e])
This program runs on training data (chrA.fasta) file, predict CpG islands based on the CpG
potential being positive or negative.

Viterbi.py: 
Input: (10_datasets.txt) A string x, followed by the alphabet from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
Output: A path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.

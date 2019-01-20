# author: kyle bogart
# desc: dna transcribing - takes dna sequence and converts to an rna sequence
# dna = raw_input("DNA Sequence: ")

def rna(dna_sequence):
	rna = dna_sequence.lower().replace('t', 'u')
	
	return rna.upper()
	


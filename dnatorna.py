def reverse_rna_complement(seq):
    #determine if original sequence is uppercase
    seq_upper = seq.isupper()

    #reverse sequence
    seq = seq [::-1]

    #convert to uppercase
    seq = seq.upper()

    #compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    if seq_upper:
        return seq.upper()
    else:
        return seq

def rna(seq):
    """Convert a DNA sequence to RNA."""

    # Determine if original sequence was uppercase
    seq_upper = seq.isupper()

    # Convert to lowercase
    seq = seq.lower()

    # Swap out 't' for 'u'
    seq = seq.replace('t', 'u')

    # Return upper or lower case RNA sequence
    if seq_upper:
        return seq.upper()
    else:
        return seq

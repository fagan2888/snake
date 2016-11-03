import palindromes
NUCLEOTIDES = 'ATCG'
ENZYMES = {'EcoRI': 'GAATTC', 'BamHI': 'GGATCC', 'HindIII': 'AAGCTT',
                'TaqI': 'TCGA', 'NotI': 'GCGGCCGC', 'Sau3A': 'GATC',
                'PovII': 'CAGCTG', 'SmaI': 'CCCGGG', 'HaeIII': 'GGCC',
                'HgaI': 'GACGC', 'AluI': 'AGCT', 'EcoRV': 'GATATC',
                'KpnI': 'GGTACC', 'PstI': 'CTGCAG', 'SacI': 'GAGCTC',
                'SalI': 'GTCGAC', 'ScaI': 'AGTACT', 'SphI': 'GCATGC',
                'StuI': 'AGGCCT', 'XbaI': 'TCTAGA'}


def is_base_pair(base1, base2):
    """ (str, str) -> bool
    
    Returns True if and only if base1 and base2 form a base pair as a string.
    i.e. if they form any of the following base pairs: 'AT', 'TA', 'CG', 'GC'
    Precondition: base1 and base2 must be one of the letters A, T, C, or G.
    
    >>>> is_base_pair('A', 'T')
    True
    >>>> is_base_pair('A', 'G')
    False
    >>>> is_base_pair('Z', 'Z')
    ''
    """
    
    basetype1 = 'AT'
    basetype2 = 'CG'
    all_base_pairs = [basetype1, basetype2, basetype1[::-1],basetype2[::-1]]
    if base1 and base2 in (basetype1 + basetype2):
        pair_candidate = base1 + base2
        return (pair_candidate or pair_candidate[::-1]) in all_base_pairs
    else:
        return ''


def is_dna(strand1, strand2):
    """ (str, str) -> bool
    
    Returns True if and only if the DNA strands strand1 and strand2 form a
    proper DNA molecule with adjacent bases between strands forming base pairs.
    Precondition: strand1 and strand2 must be of equal length and contain
    only the letters A, T, C, or G.
    
    >>>> is_dna('GGATC', 'CCTAG')
    True
    >>>> is_dna('GGCC', 'TATA')
    False
    >>>> is_dna('ZZZZ', 'XXX')
    ''
    """
    
    if len(strand1) == len(strand2):
        for char in (strand1 + strand2):
            if char in NUCLEOTIDES:
                boolean = True
                for i in range(len(strand1)):
                    boolean *= is_base_pair(strand1[i], strand2[i])
                return bool(boolean)
            else:
                return ''
    else:
        return ''


def is_dna_palindrome(strand1, strand2):
    """ (str, str) -> bool
    
    Returns True if and only if DNA strands strand1 and strand2 form a proper
    DNA molecule and forms a palindrome with their letters combined.
    Precondition: strand1 and strand2 must both be valid DNA strands.
    
    >>>> is_dna_palindrome('GGATCC', 'CCTAGG')
    True
    >>>> is_dna_palindrome('GGATC', 'CCTAG')
    False
    >>>> is_dna_palindrome('ZZZZ', 'XXX')
    ''
    """
    return is_dna(strand1, strand2) and palindromes.is_palindromic_phrase(strand1 + strand2)


def restriction_sites(strand, recog_seq):
    """ (str, str) -> list of int
    
    Returns a list of all indices in the strand where the recognition sequence
    recog_seq appears.
    Precondition: strand is a valid DNA strand.
    
    >>>> restriction_sites('GGCCGGGGCCGGCCCCGG', 'GG')
    [0, 4, 6, 10, 16]
    >>>> restriction_sites('GGCCGGGGCCGGCCCCGG', 'GG')
    [2, 8, 12, 14]
    >>> restriction_sites('FFFFFF', 'CC')
    ''
    """
    
    if set(strand) <= set(NUCLEOTIDES):
        indices = []
        count = 0
        for i in range((len(strand) // len(recog_seq)) - 1):
            index = strand.find(recog_seq, count, len(strand))
            if index not in indices and index != -1:
                indices.append(strand.find(recog_seq, count, len(strand)))
            count += len(recog_seq)
            i += 1
        return indices
    else:
        return ''


def match_enzymes(strand, enzyme_list, seq_list):
    """ (str, list of str, list of str) -> 
                    list of two-item [str, list of int] lists
    
    Returns a list of of two-item lists which, for each two-item list entry,
    categorizes the enzymes searched for in the given DNA strand argument
    and also returns the restriction sites where such enzymes occur.
    Precondition: enzyme_list and sequence_list must be parallel lists that
    validly correspond according to the enzyme dictionary. Strand must also
    be a valid DNA strand.
    
    >>> match_enzymes('GGGGAATTCCCCGAATTCAAAAGTACTAAA', 
                    ['EcoRI', 'ScaI'], ['GAATTC', 'AGTACT'])
    [['EcoRI', [3, 12]], ['ScaI', [21]]]
    >>> match_enzymes('GGGGAATTCCCCGAATTCAAAAGTACTAAA', 
                    ['EcoRI', 'SphI'], ['GAATTC', 'AGTACT'])
    ''
    >>> match_enzymes('GGGGAATTCCCCGAATTCAAAAGTACTAAA', 
                        ['EcoRI', 'ABCD'], ['ZZZZ', 'AGTACT'])
    ''
    """
    
    final_list = []
    # check if enzyme_list and seq_list are valid:
    if len(enzyme_list) == len(seq_list) and set(strand) <= set(NUCLEOTIDES):
        # check if each enzyme in the enzyme list matches to its corresponding
        # nucleotide sequence in the sequence list
        flag = True
        for i in range(len(enzyme_list)):
            if ENZYMES[enzyme_list[i]] != seq_list[i]:
                flag = False
                break
        if flag:
            # creates the final list entry for each enzyme
                for enzyme in enzyme_list:
                    list_entry = []
                    list_entry.append(enzyme)
                    list_entry.append(restriction_sites
                                    (strand, ENZYMES[enzyme]))
                    final_list.append(list_entry)
                return final_list
        else:
            return ''
    else:
        return ''


def one_cutters(strand, enzyme_list, seq_list):
    """ (str, list of str, list of str) -> 
                    list of two-item [str, list of int] lists
    
    Returns a list of two-item lists which represent the one-cutters extracted
    from a call to match_enzymes using a DNA strand, an enzyme list and its
    corresponding recognition sequence list as arguments. That is, it performs
    the function of match_enzymes outlined above, and subsequently finds the
    enzymes which occur once and only once in the DNA strand.
    Precondition: Same precondition as match_enzymes
    
    >>> one_cutters('GGGGAATTCCCCGAATTCAAAAGTACTAAA', 
                    ['EcoRI', 'ScaI'], ['GAATTC', 'AGTACT'])
    [['ScaI', [21]]]
    >>> one_cutters('GGGGAATTCCCCGAATTCAAAAGTACTAAA', 
                    ['EcoRI', 'SphI'], ['GAATTC', 'AGTACT'])
    ''
    >>> one_cutters('GGGGAATTCCCCGAATTCAAAAGTACTAAA', 
                        ['EcoRI', 'ABCD'], ['ZZZZ', 'AGTACT'])
    ''
    """
    # make a call to the original match_enzymes method, passing in the
    # arguments.
    modified_list = match_enzymes(strand, enzyme_list, seq_list)
    # iterate through each entry in the unmodified list. if the second
    # item in the entry contains more than one number, remove that entry
    for entry in modified_list:
        if len(entry[1]) > 1:
            modified_list.remove(entry)
    return modified_list


def correct_mutations(mutated_list, clean_strand, enzyme_list, seq_list):
    """ (list of str, str, list of str, list of str) -> NoneType
    
    Modifies a list of mutated strands of DNA using a clean strand of DNA and
    a list of enzymes and their corresponding recognition sequences. This is
    done by finding which one-cutters are shared by each mutated strand with
    the clean strand, and replacing the rest of the mutated strand sequence
    following the one-cutter with the clean strand's corresponding section.
    Precondition: The clean strand will contain one and only one one-cutter
    from the list of enzymes and its recognition sequence list.
    
    >>> strands = ['ACGTGGCCTAGCT', 'CAGCTGATCG']
    >>> clean = 'ACGGCCTT'
    >>> names = ['HaeIII', 'HgaI', 'AluI']
    >>> sequences = ['GGCC', 'GACGC', 'AGCT']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['ACGTGGCCTT', 'CAGCTGATCG']
    >>> strands = ['ACGTGGAGTACT', 'AGTACTCCCCCC']
    >>> clean = 'GGGGAATTCCCCGAATTCAAAAGTACTAAA'
    >>> names = ['HaeIII', 'ScaI', 'AluI']
    >>> sequences = ['GGCC', 'AGTACT', 'AGCT']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['ACGTGGAGTACTAAA', 'AGTACTAAA']
    >>> strands = ['XXXXXX', 'YYYYYY']
    >>> clean = 'ZZZZZZ'
    >>> names = ['HaeIII', 'ScaI', 'AluI']
    >>> sequences = ['GGCC', 'AGTACT', 'AGCT']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['XXXXXX', 'YYYYYY']
    """
    # we will replace mutated_list with corrected_list
    corrected_list = []
    clean_cutters = one_cutters(clean_strand, enzyme_list, seq_list)
    # isolate the single one-cutter from the clean strand
    clean_cutters = [x for x in clean_cutters if x[1] != []]
    for i in range(len(mutated_list)):
        strand = mutated_list[i]   
        entry_cut = one_cutters(strand, enzyme_list, seq_list)
        for i in range(len(entry_cut) - 1):
            # for each entry in the mutated list, it contains the one-cutter,
            # perform the mutation correction
            if entry_cut[i][0] == clean_cutters[0][0] and entry_cut[i][1] != []:
                entry_index = strand.find(ENZYMES[clean_cutters[0][0]])
                clean_index = clean_strand.find(ENZYMES[clean_cutters[0][0]])
                strand = strand.replace(strand[entry_index:], 
                                clean_strand[clean_index:])
        corrected_list.append(strand)
    mutated_list[:] = corrected_list
    
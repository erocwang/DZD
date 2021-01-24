# code for finding all similar matching kmers in a sequence 

# returns a set of kmer matches in a sequence
def pre_compute_match(kseq, seq) -> set: 
    res = set()
    if(len(kseq) > len(seq)): 
        return res 
    bases = {'A':['C','G','T'],'C':['A','G','T'],'G':['A','C','T'],'T':['A','C','G']}
    pre_computed = set() 
    pre_computed.add(kseq)

    for i in range(len(kseq)):
        temp = list(kseq)
        for j in range(3):
            temp[i] = bases[kseq[i]][j]
            pre_computed.add("".join(temp)) # add one char diffs
    for i in range(len(kseq)):
        temp = list(kseq)
        for j in range(3): 
            temp[i] = bases[kseq[i]][j]
            for k in range(i+1,len(kseq)):
                temp_copy = temp[:] 
                for l in range(3): 
                    temp_copy[k] = bases[kseq[k]][l]
                    pre_computed.add("".join(temp_copy)) # add two char diffs 
    
    for i in range(len(seq)-len(kseq)+1):
        seq_substr = seq[i:i+len(kseq)]
        if seq_substr in pre_computed:
            res.add(seq_substr)
    return res
    
# returns a set of kmer matches in a sequence
def sliding_window_match(kseq, seq) -> set: 
    res = set()
    if(len(kseq) > len(seq)): 
        return matches
    for i in range(len(seq)-len(kseq)+1):
        seq_substr = seq[i:i+len(kseq)]
        if matches(kseq,seq_substr):
            res.add(seq_substr)
    return res

# returns true if both strings differ by at most 2 characters
def matches(a , b) -> bool: 
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 2:
            return False
    return True


def orf(codons):
    orfs = []
    i = 0
    while i < len(codons):
        if codons[i] == 'AUG':
            j = i
            while j < len(codons):
                if codons[j] in ['UGA','UAG','UAA']:
                    current_orf = dict(start = i, end = j, orf = codons[i:j]) #起始和终止的都是编程里的索引
                    orfs.append(current_orf)
                    i+=1
                    break
                else:
                    j+=1
            else:
                i+=1
        else:
            i+=1
    return orfs
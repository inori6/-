import re
#初次清洗
def preliminary_data_cleaning(text):
    return re.sub(r'[^A-Za-z]', '', text.upper())

#碱基序列输入函数
def bases_input(prompt):
    input(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "done":
            break
        lines.append(line)
    bs = '\n'.join(lines)
    return bs

#mrna展示函数
def mrna_show(seq, line_width=60, group_size=10):
    result = []
    for i in range(0, len(seq), line_width):
        line_seq = seq[i:i+line_width]
        grouped = ' '.join([line_seq[j:j+group_size] for j in range(0, len(line_seq), group_size)])
        result.append(f"{i+1:>6} {grouped}")
    return '\n'.join(result)

#展示open reading frame
def display_orf(orfs,position):
    if not orfs:
        pass
    else:
        print(f'In reading frame{position}, the following open reading frame sequences were found:')
        for number,item in enumerate(orfs):
            print(f'''{number+1}    {item}''''')

#orf的寻找函数
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

#氨基酸预测函数
CODON_TABLE = {
    'AUG': 'Met',
    'UUU': 'Phe', 'UUC': 'Phe',
    'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'UAU': 'Tyr', 'UAC': 'Tyr',
    'CAU': 'His', 'CAC': 'His',
    'CAA': 'Gln', 'CAG': 'Gln',
    'AAU': 'Asn', 'AAC': 'Asn',
    'AAA': 'Lys', 'AAG': 'Lys',
    'GAU': 'Asp', 'GAC': 'Asp',
    'GAA': 'Glu', 'GAG': 'Glu',
    'UGU': 'Cys', 'UGC': 'Cys',
    'UGG': 'Trp',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser',
    'AGA': 'Arg', 'AGG': 'Arg',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}


def get_ordinal_suffix(n):
    if 10 <= n % 100 <= 20:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')


def predict_amino(orfs, n):
    aass = []
    if orfs:
        print(f'In Open Reading Frame {n}, there are {len(orfs)} possible amino acid sequences:')
    else:
        pass

    for index, item in enumerate(orfs):
        aas = [CODON_TABLE[i] for i in item]
        aass.append(aas)

        suffix = get_ordinal_suffix(index + 1)
        format_aas = '—'.join(aas)
        if orfs:
            print(f'The {index + 1}{suffix} possible amino acid sequence is: {format_aas}')
        else:
            pass

    return aass

#读取mrna序列函数
def reading_frame(mrna, n=0):
    if n in [0,1,2]:
        codons = [mrna[i:i + 3] for i in range(n, len(mrna), 3)]
        return codons
    else:
        while not n in [0,1,2]:
            n=int(input("⚠️ 你必须输入 0、1 或 2 作为 reading frame的类型:"))
        codons = [mrna[i:i+3] for i in range(n, len(mrna), 3)]
        return codons
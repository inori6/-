class DNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def show(self):
        print(f'DNA sequence: {self.sequence}')

    def complementary_strand(self):
        comp_strand = self.sequence.translate(str.maketrans('ATCG', 'TAGC'))
        print(f'Complementary strand: {comp_strand}')
        return comp_strand

    def rna_strand(self):
        rna=self.sequence.replace('T','U')
        return rna

    def num_bases(self):
        print(f'Number of bases: {len(self.sequence)}')
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[key]

    def __len__(self):
        return len(self.sequence)

    def __str__(self):
        return self.sequence

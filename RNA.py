class RNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def show(self):
        print(f'mRNA sequence: {self.sequence}')

    def num_bases(self):
        print(f'num bases: {len(self.sequence)}')

    def __getitem__(self, key):
        return self.sequence[key]

    def __len__(self):
        return len(self.sequence)

    def __str__(self):
        return self.sequence

    def gc_content(self):
        gc = self.sequence.count('G') + self.sequence.count('C')
        return gc / len(self.sequence) if len(self.sequence) > 0 else 0

    def __iter__(self):
        return iter(self.sequence)

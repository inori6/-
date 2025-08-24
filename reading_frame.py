def reading_frame(mrna, n=0):
    if n in [0,1,2]:
        codons = [mrna[i:i + 3] for i in range(n, len(mrna), 3)]
        return codons
    else:
        while not n in [0,1,2]:
            n=int(input("⚠️ 你必须输入 0、1 或 2 作为 reading frame的类型:"))
        codons = [mrna[i:i+3] for i in range(n, len(mrna), 3)]
        return codons
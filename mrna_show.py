#mrna展示函数
def mrna_show(seq, line_width=60, group_size=10):
    result = []
    for i in range(0, len(seq), line_width):
        line_seq = seq[i:i+line_width]
        grouped = ' '.join([line_seq[j:j+group_size] for j in range(0, len(line_seq), group_size)])
        result.append(f"{i+1:>6} {grouped}")
    return '\n'.join(result)
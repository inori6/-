#碱基序列输入函数
def bases_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "done":
            break
        lines.append(line)
    bs = '\n'.join(lines)
    return bs
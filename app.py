from flask import Flask, render_template, request, jsonify
from DNA import DNA
from RNA import RNA
from function import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    sequence = request.form.get('sequence', '')
    if not sequence:
        return jsonify({'error': 'No sequence provided'})

    # 清理输入序列
    seq = preliminary_data_cleaning(sequence)
    valid_bases = set('AUGTC')

    # 验证序列
    if not seq:
        return jsonify({'error': 'No valid sequence found after cleaning. Please enter a DNA or RNA sequence.'})
    if len(seq) < 3:
        return jsonify({'error': 'Sequence is too short. At least 3 bases are required to form a codon.'})
    if not set(seq).issubset(valid_bases):
        return jsonify({'error': 'Invalid sequence. Only A, U, G, T, C bases are allowed.'})
    if 'U' in seq and 'T' in seq:
        return jsonify({'error': 'Sequence cannot contain both T and U.'})

    # 确定序列类型并转换为mRNA
    if 'U' in seq and 'T' not in seq:
        seq = RNA(seq)
        sequence_type = 'RNA'
    else:
        seq = DNA(seq)
        sequence_type = 'DNA'

    # 获取mRNA序列
    if isinstance(seq, DNA):
        mrna = RNA(seq.rna_strand())
    else:
        mrna = seq

    # 获取三种reading frame
    rf1 = reading_frame(mrna, 0)
    rf2 = reading_frame(mrna, 1)
    rf3 = reading_frame(mrna, 2)
    rfs = [rf1, rf2, rf3]

    # 查找ORFs
    orfs_results = []
    for i, rf in enumerate(rfs):
        frame_orfs = []
        if orf(rf):
            for o in orf(rf):
                frame_orfs.append({
                    'sequence': ' '.join(o['orf']),
                    'start': o['start'],
                    'end': o['end']
                })
        orfs_results.append({
            'frame': i + 1,
            'orfs': frame_orfs
        })

    # 预测氨基酸序列
    amino_acids = []
    for frame_result in orfs_results:
        frame_amino = []
        for orf_seq in frame_result['orfs']:
            codons = orf_seq['sequence'].split()
            amino_seq = [CODON_TABLE[codon] for codon in codons]
            frame_amino.append('—'.join(amino_seq))
        amino_acids.append({
            'frame': frame_result['frame'],
            'sequences': frame_amino
        })

    # 准备返回结果
    result = {
        'sequence_type': sequence_type,
        'original_sequence': seq.sequence,
        'mrna_sequence': mrna_show(mrna),
        'reading_frames': [
            {'frame': i + 1, 'codons': ' '.join(rf)} for i, rf in enumerate(rfs)
        ],
        'orfs': orfs_results,
        'amino_acids': amino_acids
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
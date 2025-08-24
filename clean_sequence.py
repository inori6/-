#数据清洗函数
import re
def clean_sequence(raw):
    """清理用户输入，只保留 A/U/G/T/C"""
    return re.sub(r'[^AUGTC]', '', raw.upper())
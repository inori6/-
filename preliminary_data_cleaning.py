import re
def preliminary_data_cleaning(text):
    return re.sub(r'[^A-Za-z]', '', text.upper())
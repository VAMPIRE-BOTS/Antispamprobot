import re

def normalize_text(text):

    text = text.lower()

    text = re.sub(r"\s+", "", text)

    text = re.sub(r"[^a-zA-Z0-9]", "", text)

    text = re.sub(r'(.)\1+', r'\1', text)

    return text

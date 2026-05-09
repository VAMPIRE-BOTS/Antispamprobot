from app.helpers.cleaner import normalize_text

with open(
    "app/data/badwords.txt",
    "r",
    encoding="utf-8"
) as f:

    BAD_WORDS = set(
        line.strip().lower()
        for line in f.readlines()
        if line.strip()
    )

def detect_abuse(text):

    if not text:
        return False

    clean = normalize_text(text)

    for word in BAD_WORDS:

        if word in clean:
            return True

    return False

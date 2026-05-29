def summarize(text, max_sentences=2):
    if not text:
        return ""

    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    summary = sentences[:max_sentences]
    return ". ".join(summary) + "."

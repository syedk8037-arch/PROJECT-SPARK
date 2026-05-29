import re
from brain.synonyms import apply_synonyms

STOP_WORDS = [
     # Question starters
    "what", "why", "how", "when", "where", "who", "whom", "which",

    # Verbs & helpers
    "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did",
    "can", "could", "should", "would", "may", "might", "will",

    # Articles & determiners
    "a", "an", "the", "this", "that", "these", "those",

    # Prepositions
    "about", "of", "on", "in", "at", "for", "with", "from", "to", "by",

    # Politeness / filler
    "please", "kindly", "just", "actually", "basically",

    # Explanation verbs
    "explain", "describe", "define", "tell", "give", "show",

    # Information words
    "information", "details", "overview", "meaning", "definition",

    # Personal words (spoken language)
    "me", "my", "mine", "you", "your", "yours",

    # Common spoken fillers
    "like", "okay", "ok", "so", "uh", "um",

    # Question endings
    "mean", "means", "work", "works", "working",

    # AI-assistant style commands
    "spark", "please", "help",

    # Misc noise
    "something", "anything", "everything"
]

def normalize_question(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)

    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]

    # Apply synonym mapping
    words = apply_synonyms(words)

    # Remove duplicates & sort for stability
    words = sorted(set(words))

    return " ".join(words)

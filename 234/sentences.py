TERMINATIONS = [".", "?", "!"]
SENTENCE_SPLITTER = "----splitter----"


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
    in dot (.), question mark (?) and exclamation mark (!)"""
    for end_sentence in TERMINATIONS:
        text = text.replace(end_sentence, f"{end_sentence}{SENTENCE_SPLITTER}")
    sentences = text.split(SENTENCE_SPLITTER)
    return " ".join([sentence.strip().capitalize() for sentence in sentences]).strip()

def word_count(text: str) -> int:
    return len(text.split())

def char_count(text: str) -> dict[str: int]:
    low_text = text.lower()
    counts: dict[str: int] = {}
    for ch in low_text:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts
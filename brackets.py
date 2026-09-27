PAIRS = {")": "(", "]": "[", "}": "{"}
OPENERS = "([{"


def first_mismatch(text: str) -> int | None:
    """Index of the first bracket that does not close its pair. None when the text is fine."""
    stack: list[tuple[str, int]] = []
    for index, ch in enumerate(text):
        if ch in OPENERS:
            stack.append((ch, index))
        elif ch in PAIRS:
            if not stack or stack.pop()[0] != PAIRS[ch]:
                return index
    if stack:
        return stack[0][1]
    return None


def mismatch_kind(text: str) -> str:
    """ok, closer (a closing mark with no pair), or open (an opener left hanging)."""
    index = first_mismatch(text)
    if index is None:
        return "ok"
    if text[index] in PAIRS:
        return "closer"
    return "open"


def brackets_balanced(text: str) -> bool:
    return first_mismatch(text) is None

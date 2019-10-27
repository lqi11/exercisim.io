def is_isogram(string):
    character_lower = [c.lower() for c in string if c.isalpha()]
    return len(set(character_lower)) == len(character_lower)

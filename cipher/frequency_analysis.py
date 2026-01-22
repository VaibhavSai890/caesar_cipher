def detect_shift(text):
    frequency = {}

    for char in text.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    if not frequency:
        return 0

    most_common = max(frequency, key=frequency.get)

    detected_shift = (ord(most_common) - ord('e')) % 26
    return detected_shift

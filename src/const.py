table = {
    0: { '\n': 0, ' ': 0, '[': 1, ',': 2, ']': 3, '=': 4, '"': 5, '-': 10, '.': 12,
        '0': 11, '1': 11, '2': 11, '3': 11, '4': 11, '5': 11, '6': 11, '7': 11, '8': 11, '9': 11,
        'a': 7, 'b': 7, 'c': 7, 'd': 7, 'e': 7, 'f': 7, 'g': 7, 'h': 7, 'i': 7, 'j': 7,
        'k': 7, 'l': 7, 'm': 7, 'n': 7, 'o': 7, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 7, 'u': 7,
        'v': 7, 'w': 7, 'x': 7, 'y': 7, 'z': 7, 'A': 7, 'B': 7, 'C': 7, 'D': 7, 'E': 7, 'F': 7,
        'G': 7, 'H': 7, 'I': 7, 'J': 7, 'K': 7, 'L': 7, 'M': 7, 'N': 7, 'O': 7, 'P': 7, 'Q': 7,
        'R': 7, 'S': 7, 'T': 7, 'U': 7, 'V': 7, 'W': 7, 'X': 7, 'Y': 7, 'Z': 7 },

    5: { '"': 6, 'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5, 'f': 5, 'g': 5, 'h': 5, 'i': 5, 'j': 5,
        'k': 5, 'l': 5, 'm': 5, 'n': 5, 'o': 5, 'p': 5, 'q': 5, 'r': 5, 's': 5, 't': 5, 'u': 5,
        'v': 5, 'w': 5, 'x': 5, 'y': 5, 'z': 5, 'A': 5, 'B': 5, 'C': 5, 'D': 5, 'E': 5, 'F': 5,
        'G': 5, 'H': 5, 'I': 5, 'J': 5, 'K': 5, 'L': 5, 'M': 5, 'N': 5, 'O': 5, 'P': 5, 'Q': 5,
        'R': 5, 'S': 5, 'T': 5, 'U': 5, 'V': 5, 'W': 5, 'X': 5, 'Y': 5, 'Z': 5, '0': 5, '1': 5,
        '2': 5, '3': 5, '4': 5, '5': 5, '6': 5, '7': 5, '8': 5, '9': 5, ' ': 5, '.': 5, ',': 5 },

    7: { '=': 9, ' ': 8, '\n': 8, ']': 17,
        'a': 7, 'b': 7, 'c': 7, 'd': 7, 'e': 7, 'f': 7, 'g': 7, 'h': 7, 'i': 7, 'j': 7,
        'k': 7, 'l': 7, 'm': 7, 'n': 7, 'o': 7, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 7, 'u': 7,
        'v': 7, 'w': 7, 'x': 7, 'y': 7, 'z': 7, 'A': 7, 'B': 7, 'C': 7, 'D': 7, 'E': 7, 'F': 7,
        'G': 7, 'H': 7, 'I': 7, 'J': 7, 'K': 7, 'L': 7, 'M': 7, 'N': 7, 'O': 7, 'P': 7, 'Q': 7,
        'R': 7, 'S': 7, 'T': 7, 'U': 7, 'V': 7, 'W': 7, 'X': 7, 'Y': 7, 'Z': 7, '0': 7, '1': 7,
        '2': 7, '3': 7, '4': 7, '5': 7, '6': 7, '7': 7, '8': 7, '9': 7 },

    10: { '0': 11, '1': 11, '2': 11, '3': 11, '4': 11, '5': 11, '6': 11, '7': 11, '8': 11, '9': 11 },

    11: { '0': 11, '1': 11, '2': 11, '3': 11, '4': 11, '5': 11, '6': 11, '7': 11, '8': 11, '9': 11,
        '.': 12, ' ': 14, ',': 15, ']': 16, '\n': 14 },

    12: { '0': 13, '1': 13, '2': 13, '3': 13, '4': 13, '5': 13, '6': 13, '7': 13, '8': 13, '9': 13 },

    13: { '0': 13, '1': 13, '2': 13, '3': 13, '4': 13, '5': 13, '6': 13, '7': 13, '8': 13, '9': 13,
        ' ': 14, ',': 15, ']': 16, '\n': 14 },
}
finals = {
    1: 'SQ_ST',
    2: 'CM',
    3: 'SQ_ED',
    4: 'EQ',
    6: 'STR',
    8: 'KEY',
    9: ['KEY', 'EQ'],
    14: 'NUM',
    15: ['NUM', 'CM'],
    16: ['NUM', 'SQ_ED'],
    17: ['KEY', 'SQ_ED']
}

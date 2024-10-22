def getDistance(word):
    distance = 0
    rows = { 'Q': 0, 'W': 0, 'E': 0, 'R': 0, 'T': 0, 'Y': 0, 'U': 0, 'I': 0, 'O': 0, 'P': 0, 'A': 1, 'S': 1, 'D': 1, 'F': 1, 'G': 1, 'H': 1, 'J': 1, 'K': 1, 'L': 1, 'Z': 2, 'X': 2, 'C': 2, 'V': 2, 'B': 2, 'N': 2, 'M': 2 }

    columns = { 'Q': 0, 'W': 1, 'E': 2, 'R': 3, 'T': 4, 'Y': 5, 'U': 6, 'I': 7, 'O': 8, 'P': 9, 'A': 0, 'S': 1, 'D': 2, 'F': 3, 'G': 4, 'H': 5, 'J': 6, 'K': 7, 'L': 8, 'Z': 1, 'X': 2, 'C': 3, 'V': 4, 'B': 5, 'N': 6, 'M': 7 }

    if word[0] != 'Q':
        word = 'Q' + word
        
    for i in range(1, len(word)):
        distance += abs(rows[word[i]] - rows[word[i - 1]]) + abs(columns[word[i]] - columns[word[i - 1]])
    
    return distance

if __name__ == '__main__':
    print(getDistance('HELLO'))
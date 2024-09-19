from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        repeated_dna_sequences = []
        c = Counter([s[i:10+i] for i in range(len(s)-9)])
        for key, count in c.items():
            if count > 1:
                repeated_dna_sequences.append(key)
            
        return repeated_dna_sequences

from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        repeated_dna_sequences = set()
        sequences = set()
        for i in range(len(s)-9):
            sequence = s[i:10+i]
            if sequence in sequences:
                repeated_dna_sequences.add(sequence)
            else:
                sequences.add(sequence)
            
        return repeated_dna_sequences

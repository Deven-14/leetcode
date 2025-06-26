class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new_sentence = []
        for i, word in enumerate(sentence.split(), start=1):
            if word[0] in 'aeiouAEIOU':
                new_sentence.append(word + "ma" + 'a' * i)
            else:
                new_sentence.append(word[1:] + word[0] + "ma" + 'a' * i)
        
        return " ".join(new_sentence)
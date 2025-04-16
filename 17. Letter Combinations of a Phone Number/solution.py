from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digits_to_letters = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        list_of_letters = [digits_to_letters[int(digit)] for digit in digits]
        combinations = product(*list_of_letters)
        return ["".join(combination) for combination in combinations]


class Solution:

    def letter_combinations(self, list_of_letters, combinations, combination: list = [], i: int = 0):
        if i == len(list_of_letters):
            combinations.append("".join(combination))
            return
        
        for letter in list_of_letters[i]:
            combination.append(letter)
            self.letter_combinations(list_of_letters, combinations, combination, i+1)
            combination.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digits_to_letters = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        list_of_letters = [digits_to_letters[int(digit)] for digit in digits]
        combinations = []
        self.letter_combinations(list_of_letters, combinations)

        return combinations


class Solution:

    def letter_combinations(self, list_of_letters, combinations, combination: str = "", i: int = 0):
        if i == len(list_of_letters):
            combinations.append(combination)
            return
        
        for letter in list_of_letters[i]:
            self.letter_combinations(list_of_letters, combinations, combination + letter, i+1)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digits_to_letters = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        list_of_letters = [digits_to_letters[int(digit)] for digit in digits]
        combinations = []
        self.letter_combinations(list_of_letters, combinations)

        return combinations



class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digits_to_letters = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        list_of_letters = [digits_to_letters[int(digit)] for digit in digits]
        combinations = [[]]
        
        for letters in list_of_letters:
            combinations = [
                combination + [letter]
                for letter in letters
                for combination in combinations
            ]

        return ["".join(combination) for combination in combinations]
class MagicDictionary:

    def __init__(self):
        self.mdict = defaultdict(set)

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                self.mdict[word[:i] + "*" + word[i + 1:]].add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            word = searchWord[:i] + "*" + searchWord[i + 1:]
            if word in self.mdict and (searchWord not in self.mdict[word] or len(self.mdict[word]) > 1):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
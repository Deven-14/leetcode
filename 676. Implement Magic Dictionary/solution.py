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




# ! very very slow (below one)

class MagicDictionary:

    def __init__(self):
        self.mdict = set()

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    if char != word[i]:
                        self.mdict.add(word[:i] + char + word[i + 1:])

    def search(self, searchWord: str) -> bool:
        return searchWord in self.mdict


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


class MagicDictionary:

    def __init__(self):
        self.mdict = Counter()

    def buildDict(self, dictionary: list[str]) -> None:
        self.words = set(dictionary)
        for word in dictionary:
            for i in range(len(word)):
                self.mdict[word[:i] + "*" + word[i + 1:]] += 1

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            word = searchWord[:i] + "*" + searchWord[i + 1:]
            if self.mdict[word] > 1 or (self.mdict[word] == 1 and searchWord not in self.words):
                return True
        return False


class MagicDictionary:

    def __init__(self):
        self.mdict = defaultdict(list)

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            self.mdict[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.mdict[len(searchWord)]:
            if self._match(word, searchWord):
                return True
        
        return False
    
    def _match(self, word, searchWord):
        if len(word) != len(searchWord): return False
        mismatch = 0
        
        for a, b in zip(word, searchWord):
            if a != b:
                mismatch += 1
                if mismatch > 1:
                    return False
        
        return mismatch != 0
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_breaks = []
        word_break = []
        
        def helper(s):
            if len(s) == 0:
                word_breaks.append(" ".join(word_break))
                return
            
            for word in wordDict:
                if s.startswith(word):
                    word_break.append(word)
                    helper(s[len(word):])
                    word_break.pop()
        
        helper(s)
        return word_breaks


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        @cache
        def helper(s):
            if len(s) == 0:
                return [""]

            word_breaks = []
            for word in wordDict:
                if s.startswith(word):
                    sub_word_breaks = helper(s[len(word):])
                    word_with_space = word + " "

                    for sub_word_break in sub_word_breaks:
                        if sub_word_break != "":
                            complete_word = word_with_space + sub_word_break
                        else:
                            complete_word = word + sub_word_break
                        word_breaks.append(complete_word)
            
            return word_breaks
        
        return helper(s)

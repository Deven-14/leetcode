class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        word_patterns = defaultdict(list)
        pattern_words = defaultdict(list)

        wordSet.add(beginWord)
        for word in wordSet:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i + 1:]}'
                word_patterns[word].append(pattern)
                pattern_words[pattern].append(word)
                
        count = 1
        queue = deque([beginWord])
        wordSet.discard(beginWord)

        while queue:
            curr_queue = queue
            next_queue = deque()

            while curr_queue:

                word = curr_queue.popleft()
                if word == endWord:
                    return count
                
                for pattern in word_patterns[word]:
                    for next_word in pattern_words[pattern]:
                        if next_word not in wordSet:
                            continue
                        next_queue.append(next_word)
                        wordSet.remove(next_word)
                        
            count += 1
            queue = next_queue

        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        word_patterns = defaultdict(list)
        pattern_words = defaultdict(list)

        wordSet.add(beginWord)
        for word in wordSet:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i + 1:]}'
                word_patterns[word].append(pattern)
                pattern_words[pattern].append(word)
                
        count = 1
        queue = deque([beginWord])
        wordSet.discard(beginWord)

        while queue:
            curr_queue = queue
            next_queue = deque()

            while curr_queue:

                word = curr_queue.popleft()
                for pattern in word_patterns[word]:
                    for next_word in pattern_words[pattern]:

                        if next_word not in wordSet:
                            continue

                        if next_word == endWord:
                            return count + 1
                        
                        next_queue.append(next_word)
                        wordSet.remove(next_word)
                        
            count += 1
            queue = next_queue

        return 0


# * BFS AND NOT DFS
# * because 
# * A -> B -> C -> D := steps 4
# * A -> C -> D := steps 3
# * if we can go directly from A -> C
# * then we don't need to visite the A -> B -> C case
# * in dfs we would do both the cases
# * but in bfs, we skip A -> B -> C case
# * we do A -> C case

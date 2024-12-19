import functools


class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = 0


def solve():
    N = 402         # number of lines of input
    available_towel_patterns = set(input().split(', '))
    desired_patterns = []

    for _ in range(N - 1):
        t = input()
        if not t: continue
        desired_patterns.append(t)


    def add_word_to_trie(word):
        cur = root

        for c in word:
            if c not in cur.kids:
                cur.kids[c] = TrieNode()
            cur = cur.kids[c]
        
        cur.end = 1

    
    def can_make(pattern):

        @functools.cache
        def dp(i, cur):
            if i >= len(pattern):
                return True
            
            res = False

            for j in range(i, len(pattern)):
                if pattern[j] not in cur.kids:
                    break
                
                cur = cur.kids[pattern[j]]
                if cur.end:
                    res |= dp(j + 1, root)
            
            return res
        
        return dp(0, root)

    root = TrieNode()
    for p in available_towel_patterns:
        add_word_to_trie(p)

    return sum(can_make(p) for p in desired_patterns)


print(solve())
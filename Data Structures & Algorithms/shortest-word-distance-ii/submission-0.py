from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.wordsDict[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        words1 = self.wordsDict[word1]
        words2 = self.wordsDict[word2]
        shortest = float('inf')
        for w in words1:
            for w2 in words2:
                gap = abs(w - w2)
                shortest = min(shortest, gap)
        
        return shortest

        




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

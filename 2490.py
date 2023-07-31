class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if not sentence:
            return True
        if sentence[0] != sentence[-1]:
            return False
        words = sentence.split(" ")
        for i in range(len(words) - 1):
            if words[i+1][0] != words[i][-1]:
                return False
        return True

sol = Solution()
print(sol.isCircularSentence("Leetcode is cool"))
'LeetCode 412 Keyboard Row'
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
          w = set(word.lower())
          if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
            ret.append(word)
        return ret
if __name__ == '__main__':
    d = ["Hello","Alaska","Dad","Peace"]
    s = Solution()
    s.findWords(d)

    
import time

class Solution:
  def lengthOfLongestSubstring(self, s):
    if not s:
    	return 0
    
    if len(s) == 1:
    	return 1

    slow = 0
    fast = 0
    letters = set([s[slow]])
    maxx = 1

    while fast < len(s) and slow <= fast:
        while fast+1 < len(s) and not s[fast+1] in letters:
            fast += 1
            letters.add(s[fast])
            print(s[slow:fast+1])
            time.sleep(.5)

        slow += 1
        fast += 1
        maxx = max(maxx, fast-slow)
        print(s[slow:fast+1])

        while fast < len(s) and slow < fast and s[slow] != s[fast]:
            print('- ', print(s[slow:fast+1]))
            letters.remove(s[slow])
            slow += 1
            time.sleep(.5)
        print(letters, slow, fast)
        time.sleep(.5)

    return maxx

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10

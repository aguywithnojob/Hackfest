# Solution to find lenght of longest substring.
# Its leet code problem.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n in [0,1] or n == len(set(s)):
            return n
    
        res = 0

        for i in range(n):
            visited = [0] * 256 
            print(i)

            for j in range(i, n):

                if (visited[ord(s[j])] == True):
                    break

                else:
                    res = max(res, j - i + 1)
                    visited[ord(s[j])] = True
            visited[ord(s[i])] = False

        return res
        

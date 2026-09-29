class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            if s[i] in count_s:
                count_s[s[i]] += 1
            else:
                count_s[s[i]] = 1
        for j in range(len(t)):
            if t[j] in count_t:
                count_t[t[j]] += 1
            else:
                count_t[t[j]] = 1
        counts_s = dict(sorted(count_s.items()))
        counts_t = dict(sorted(count_t.items()))
        return counts_s == counts_t
        
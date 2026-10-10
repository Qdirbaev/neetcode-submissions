class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        st = set()
        top = 0
        while j < len(s):
            if s[j] in st:
                while s[i] != s[j]:
                    st.remove(s[i])
                    i+=1
                st.remove(s[i])
                i+=1
                st.add(s[j])
                j+=1
            else:
                st.add(s[j])
                j+=1
            top = max(top, len(st))
        return top
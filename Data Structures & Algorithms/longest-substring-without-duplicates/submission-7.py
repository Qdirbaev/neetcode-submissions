class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        st = set()
        top = 0
        # FIRST SUCCESS
        # while j < len(s):
        #     if s[j] in st:
        #         while True:
        #             if s[i] == s[j]:
        #                 st.remove(s[i])
        #                 i+=1
        #                 break
        #             else:
        #                 st.remove(s[i])
        #                 i+=1
        #         st.add(s[j])
        #         j+=1
        #     else:
        #         st.add(s[j])
        #         j+=1
        #     top = max(top, len(st))

        while j < len(s):
            while s[j] in st:
                st.remove(s[i])
                i+=1
            st.add(s[j])
            j+=1
            top = max(top, len(st))

        return top
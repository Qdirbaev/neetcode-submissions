class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 
        # strs[word_loop_index][letter]

        res = ''
        shortest = min(strs)
        for i in range(len(shortest)):
            cur_let = shortest[i]
            for word in strs:
                if word[i] != cur_let:
                    return res
            res += cur_let

        return res



    
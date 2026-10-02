class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded = ""
        for s in strs:
            self.encoded += f'№' + s
        return self.encoded
        
    def decode(self, s: str) -> List[str]:
        res = []
        indexes = [i for i,x in enumerate(self.encoded) if x == "№"] + [len(self.encoded)]
        for index in range(len(indexes) - 1):
            word = self.encoded[(indexes[index] + 1):(indexes[index + 1])]
            res.append(word)
        return res
            



        
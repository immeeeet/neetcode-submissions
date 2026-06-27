class Solution:

    def encode(self, strs: List[str]) -> str:
        k = ""
        for i in strs:
            k = k+ i + "."
        return k
    def decode(self, s: str) -> List[str]:
        idk = s.split('.')
        return idk[:-1]
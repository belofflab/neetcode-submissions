import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        return json.loads(strs)

    def decode(self, s: str) -> List[str]:
        return json.dumps(s)

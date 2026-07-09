class Solution:

    def encode(self, strs: List[str]) -> str:
        
        line_separator = "•"

        # counters
        nullCounter = "!!"
        emptyCounter = "##"

        if strs == []:
            return nullCounter
        elif strs == [""]:
            return emptyCounter
        else:
            return line_separator.join(strs)

    def decode(self, s: str) -> List[str]:
        line_separator = "•"

        # counters
        nullCounter = "!!"
        emptyCounter = "##"

        if s == nullCounter:
            return []
        elif s == emptyCounter:
            return [""]
        else:
            return s.split(line_separator)

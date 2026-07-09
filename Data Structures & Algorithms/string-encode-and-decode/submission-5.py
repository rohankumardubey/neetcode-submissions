class Solution:

    def encode(self, strs: List[str]) -> str:
        line_seperator = "ª"

        #counter
        null_counter = "º"
        empty_counter = "¶"

        if strs == []:
            return null_counter
        elif strs == [""]:
            return empty_counter
        else:
            return line_seperator.join(strs)
        


    def decode(self, s: str) -> List[str]:
        line_seperator = "ª"

        #counter
        null_counter = "º"
        empty_counter = "¶"

        if s == null_counter:
            return []
        elif s == empty_counter:
            return [""]
        else:
            return s.split(line_seperator)


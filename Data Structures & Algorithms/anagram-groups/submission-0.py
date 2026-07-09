class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        result = []
        for element in strs:
            transform = "".join(sorted(element))
            if transform in lookup:
                getList = lookup[transform]
                getList.append(element)
            else:
                createList = []
                createList.append(element)
                lookup[transform] = createList

        for values in lookup.values():
            result.append(values)

        return result
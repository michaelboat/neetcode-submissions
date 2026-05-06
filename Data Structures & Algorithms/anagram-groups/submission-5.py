class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                arr[idx] += 1
            arr_key = tuple(arr)
            if arr_key not in map:
                map[arr_key] = []
            map[arr_key].append(word)

        return list(map.values())
        
        
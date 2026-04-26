class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count_arr = [0] * 26

            for letter in word:
                count_arr[ord(letter) - ord("a")] += 1

            result[tuple(count_arr)].append(word)

        return list(result.values())
                
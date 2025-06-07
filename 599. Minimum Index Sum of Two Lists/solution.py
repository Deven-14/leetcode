class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = set(list1) & set(list2)
        list1_indexes = {string: index for index, string in enumerate(list1)}
        list2_indexes = {string: index for index, string in enumerate(list2)}

        min_index_sum = min(list1_indexes[string] + list2_indexes[string] for string in common_strings)
        return [string for string in common_strings if list1_indexes[string] + list2_indexes[string] == min_index_sum]
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            new_arr = arr[i+1 : len(arr)]
            if len(new_arr) == 0:
                arr[i] = -1
            else:
                arr[i] = max(new_arr)
        return arr
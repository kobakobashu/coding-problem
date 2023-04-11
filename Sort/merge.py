from typing import List


class Merge:
    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)
    
    def merge(self, left, right):
        merged = []
        l_i, r_i = 0, 0
        while l_i < len(left) and r_i < len(right):
            if left[l_i] < right[r_i]:
                merged.append(left[l_i])
                l_i += 1
            else: 
                merged.append(right[r_i])
                r_i += 1
        
        if l_i < len(left):
            merged.extend(left[l_i:])
        if r_i < len(right):
            merged.extend(right[r_i:])
        
        return merged


if __name__ == "__main__":
    print(Merge().merge_sort([1,4,2,10,6,7]))

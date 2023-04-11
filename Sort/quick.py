from typing import List


class Quick:
    def quick_sort(self, arr: List[int]) -> List[int]:
        left = []
        right = []
        if len(arr) <= 1:
            return arr
        
        ref = arr[0]
        ref_count = 0

        for ele in arr:
            if ele < ref:
                left.append(ele)
            elif ele > ref:
                right.append(ele)
            else: 
                ref_count += 1
        
        left = self.quick_sort(left)
        right = self.quick_sort(right)
        return left + [ref] * ref_count + right


if __name__ == "__main__":
    target = [27, 12, 9, 7, 10]
    print(Quick().quick_sort(target))

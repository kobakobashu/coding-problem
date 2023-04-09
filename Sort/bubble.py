from typing import List


class Bubble:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            for j in range(1, len(arr) - i):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        
        return arr


if __name__ == "__main__":
    target = [27, 12, 9, 7, 10]
    # i = 0, [12, 9, 7, 10, 27]
    # i = 1, [9, 7, 10, 12, 27]
    # i = 2,
    # i = 3,
    print(Bubble().bubble_sort(target))

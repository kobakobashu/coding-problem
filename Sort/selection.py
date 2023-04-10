from typing import List


class Selection:
    def selection_sort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            cur_min = float("inf")
            mid_idx = None
            for j in range(i, len(arr)):
                if arr[j] < cur_min:
                    mid_idx = j
                    cur_min = arr[j]

            arr[i], arr[mid_idx] = arr[mid_idx], arr[i]

        return arr


if __name__ == "__main__":
    target = [27, 12, 9, 7, 10]
    print(Selection().selection_sort(target))

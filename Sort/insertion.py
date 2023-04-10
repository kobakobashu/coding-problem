from typing import List


class Insertion:
    def insertion_sort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            j = i - 1
            ele = arr[i]
            while j >= 0 and arr[j] > ele:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = ele
            print(arr)
        
        return arr


if __name__ == "__main__":
    print(Insertion().insertion_sort([1,4,2,10,6,7]))

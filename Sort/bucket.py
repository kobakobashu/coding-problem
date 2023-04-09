from typing import List


class Bucket:
    def bucket_sort(self, arr: List[int]) -> List[int]:
        bucket_arr = [0] * 30
        for num in arr:
            bucket_arr[num] = 1

        arr_idx = 0
        for idx, num in enumerate(bucket_arr):
            if num:
                arr[arr_idx] = idx
                arr_idx += 1

        return arr


if __name__ == "__main__":
    target = [27, 12, 9, 7, 10]
    print(Bucket().bucket_sort(target))

from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i, j = 0, len(nums)
    while i < j:
        if nums[i] == val:
            nums[i] = nums[j - 1]
            j -= 1
        else:
            i += 1
    return j


if __name__ == '__main__':
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

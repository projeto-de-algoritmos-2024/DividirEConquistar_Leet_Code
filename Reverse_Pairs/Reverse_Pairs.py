from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums: List[int], low: int, high: int) -> int:
            if low >= high:
                return 0
            mid = low + (high - low) // 2
            count = mergeSort(nums, low, mid) + mergeSort(nums, mid + 1, high)
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            left, right = low, mid + 1
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    left += 1
                else:
                    nums[low:high + 1] = sorted(nums[low:high + 1])
                    break
            return count
        return mergeSort(nums, 0, len(nums) - 1)

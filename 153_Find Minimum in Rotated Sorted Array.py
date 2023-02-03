class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        def find_min_number(l, r, res=float('inf')):
            mid = (l + r) // 2
            res = min(nums[mid], res)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

            if not (l < r):
                res = min(res, nums[l])
                return res

            return find_min_number(l, r, res)

        return find_min_number(l, r)

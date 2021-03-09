class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_2 = nums[i] + nums[j]
                if abs(sum_2) > 10 ** 5:
                    continue

                if -sum_2 in nums[j + 1:]:
                    to_add = [nums[i], nums[j], -sum_2]
                    if to_add in res:
                        continue
                    else:
                        res.append(to_add)

        return res
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans^=nums[i]
        rightmost = (ans&(ans-1))^ans
        ans1,ans2 = 0, 0
        for i in range(n):
            if nums[i] & rightmost:
                ans1^=nums[i]
            else:
                ans2^=nums[i]
        return [ans1,ans2] if ans1<ans2 else [ans2,ans1]
        
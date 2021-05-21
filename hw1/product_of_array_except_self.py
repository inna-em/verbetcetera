class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # накопленное произведение слева направо
        prod_1 = [nums[0]]
        for num in nums[1::]:
            prod_1.append(prod_1[-1]*num)
        # и справа налево
        prod_2 = [nums[-1]]
        for num in nums[-2:-len(nums)-1:-1]:
            prod_2.append(prod_2[-1]*num)
        result = [prod_2[-2]]
        for i in range(1, len(nums)-1):
            result.append(prod_1[i-1]*prod_2[-i-2])
        result.append(prod_1[-2])
        return result

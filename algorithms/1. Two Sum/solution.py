def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in already_seen:
                return [already_seen[need], i]
            already_seen[num] = i

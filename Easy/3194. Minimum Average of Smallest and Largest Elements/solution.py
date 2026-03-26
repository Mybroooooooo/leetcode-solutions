def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        while len(nums) > 0:
            max_ind = 0
            min_ind = 0
            for i in range(len(nums)):
                if nums[i] > nums[max_ind]:
                    max_ind = i
                if nums[i] < nums[min_ind]:
                    min_ind = i
            a = (nums[min_ind] + nums[max_ind])/2
            for idx in sorted([min_ind, max_ind], reverse=True):
                nums.pop(idx)
            averages.append(a)
        
        return min(averages)

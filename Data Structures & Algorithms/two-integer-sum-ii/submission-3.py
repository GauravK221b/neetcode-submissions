class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            diff = target - numbers[i]
            for j in range(i+1,len(numbers)):
                if numbers[j] == diff:
                    res.append(i+1)
                    res.append(j+1)
                    break
        return res

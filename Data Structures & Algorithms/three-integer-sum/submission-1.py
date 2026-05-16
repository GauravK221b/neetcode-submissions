class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()   
        sortNum = sorted(nums)
        for i in range(len(sortNum)):
            tmp = sortNum[i]
            l = i + 1 
            r = len(sortNum) - 1
           
            while l < r:
                if tmp + sortNum[l] + sortNum[r] < 0:
                    l += 1
                elif tmp + sortNum[l] +sortNum[r] > 0:
                    r -= 1
                else:
                    triplet = sorted([tmp,sortNum[l],sortNum[r]])

                    res.add(tuple(triplet))
                    l += 1
                    r -= 1
        
        return [list(t) for t in res]
 

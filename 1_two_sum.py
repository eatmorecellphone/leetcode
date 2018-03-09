class Solution:
    def twoSums(self,nums,target):
        map={}
        for i,num in enumerate(nums):
            if target-num in map:
                return(map[target-num]+1,i+1)
            d[num]=i
            

def TwoSum(nums,t):
    nums.sort()
    p1=0
    p2=len(nums)-1
    while p1<p2:
        dif=nums[p1]+nums[p2]-t
        if dif<0:
            p1+=1
        elif dif>0:
            p2-=1
        elif dif==0:
            return [nums[p1],nums[p2]]

def TwoSum1(nums,target):
        d={}
        for i in range(0,len(nums)):
            n=nums[i]
            if n in d:
                return [d[n],i]
            else:
                d[target-n]=i

print(TwoSum1([15,-6, 7, 11],9))

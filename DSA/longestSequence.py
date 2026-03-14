def longestSubsequence(nums):
    n=len(nums)
    tot=0
    isNonZero=False
    for i in nums:
        tot^=i
        if i!=0:
            isNonZero=True
    if tot!=0:
        return n
    if isNonZero:
        return n-1
    return 0
print(longestSubsequence([0,0,0,2,3,4]))
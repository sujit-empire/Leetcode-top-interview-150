class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        outlist = []
        for i in nums:
            if i not in outlist:
                outlist.append(i)
        outlist.sort()
        print(f"{len(outlist)}, nums = {outlist}")

checkdup = Solution()
checkdup.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

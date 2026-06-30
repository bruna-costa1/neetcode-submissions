class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenght= len(nums);
        nums.sort();

        # Compares current and next element to find duplicates
        for i in range (lenght-1):
             if nums[i] == nums[i+1]: 
                    return True #return true if duplicate found

        return False; # return false if duplicate not found


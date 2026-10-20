public class Solution {
    public bool hasDuplicate(int[] nums) {
        Array.Sort(nums);
        bool hasDuplicate = false;
        for (int i = 0; i < nums.Length - 1; i++)
        {
            if (nums[i] == nums[i + 1])
            {
                hasDuplicate = true;
                break;
            } 
        }
        return hasDuplicate;
    }
}
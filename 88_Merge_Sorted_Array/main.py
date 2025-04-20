class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        for i in range(m, n + 1):
            if i >= m:
                nums1[i] = nums2[i-m]

        nums1.sort()


## C# Solution
## public static void Merge(int[] nums1, int m, int[] nums2, int n)
#for (var i = 0; i < m + n; i++)
    #if (i >= m)
    #{
    #nums1[i] = nums2[i-m]
    #}
    #Array.Sort(nums1);
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        new_nums1 = nums1[0:m]

        p1,p2=0,0

        for i in range(m+n):
            elem1 = new_nums1[p1] if p1 < len(new_nums1) else float('inf')
            elem2 = nums2[p2] if p2 < len(nums2) else float('inf')

            if elem1 > elem2 :
                nums1[i] = elem2
                p2 += 1
            else:
                nums1[i] = elem1
                p1 += 1
        return nums1
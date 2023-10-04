class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # sort
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        
        # two-pointer
        i,j = 0,0
        
        intersections = []
        while (i < len(nums1)) and (j < len(nums2)):
            x1 = nums1[i]
            x2 = nums2[j]
            
            if x1 == x2:
                intersections.append(x1)
                i += 1
                j += 1
            elif x1 > x2:
                j += 1
            else:
                i += 1
        
        return intersections
            
            
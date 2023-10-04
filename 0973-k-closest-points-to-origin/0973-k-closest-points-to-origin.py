class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        dists = []
        for point in points:
            x, y = point
            dist = x*x + y*y 
            dists.append(dist)
            
        sort_idxs = [x[0] for x in sorted(enumerate(dists), key=lambda x:x[1])]
        
        closest_points = []
        for idx in range(k):
            close_idx = sort_idxs[idx]
            closest_points.append(points[close_idx])
        
        return closest_points
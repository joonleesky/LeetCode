class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        starts = []
        ends = []
        
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
            
        # sort 'starts' and re-order 'ends' based on starts
        sort_idxs = [val[0] for val in sorted(enumerate(starts), key=lambda x:x[1])]
        _starts = []
        _ends = []
        for idx in sort_idxs:
            _starts.append(starts[idx])
            _ends.append(ends[idx])
        
        starts = _starts
        ends = _ends
        
        # merge overlapping intervals
        intervals = []
        
        for idx in range(len(starts)-1):
            start_i, end_i = starts[idx], ends[idx]
            start_i_1, end_i_1 = starts[idx+1], ends[idx+1]
            
            if end_i >= start_i_1:
                starts[idx+1] = starts[idx] # merge
                ends[idx+1] = max(end_i, end_i_1)
            else:
                intervals.append([start_i, end_i])
                
        intervals.append([starts[-1], ends[-1]])

        return intervals
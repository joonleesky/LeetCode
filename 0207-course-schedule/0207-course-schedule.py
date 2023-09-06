class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # exception
        if len(prerequisites) == 0:
            return True
        
        # construct directed graphs
        edges = {}
        for (a, b) in prerequisites:
            if a not in edges:
                edges[a] = []
            edges[a].append(b)
        
        # traverse with dfs
        stack = []
        stack.append([next(iter(edges))])
            
        while (len(edges) > 0):
            schedule = stack.pop()
            a = schedule[-1]

            if a in edges:
                bs = edges[a]
                b = bs[0]
                bs.remove(b)
                if len(bs) == 0:
                    del edges[a]
                    
                new_schedule = schedule + [b]
                
                if b in schedule:
                    return False
                
            else:
                if len(stack) == 0:
                    new_schedule = [next(iter(edges))]
                
            stack.append(new_schedule)
                
        return True
        
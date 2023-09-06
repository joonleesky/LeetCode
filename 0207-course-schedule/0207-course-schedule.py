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
        edges = collections.defaultdict(list)
        for (a, b) in prerequisites:
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
                
                if b in schedule:
                    return False
                
                edges[a].remove(b)
                if len(edges[a]) == 0:
                    del edges[a]
                
                new_schedule = schedule + [b]
                
            else:
                if len(stack) == 0:
                    new_schedule = [next(iter(edges))]
                
            stack.append(new_schedule)
                
        return True
        
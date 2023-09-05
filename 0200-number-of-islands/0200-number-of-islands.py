class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        #####################
        # construct graph
        vertices = {}
        edges = {}
        
        # assign vertices
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    vertices[(i,j)] = len(vertices)
        
        for vertex_idx in vertices.values():
            edges[vertex_idx] = []
        
        
        # assign edges
        for (i,j), vertex_idx in vertices.items():
            candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for candidate in candidates:
                if candidate in vertices:
                    candidate_idx = vertices[candidate]
                    edges[vertex_idx].append(candidate_idx)
                    
        # handle exception
        if len(vertices) == 0:
            return 0
        
        ##################
        # perform dfs
        unvisited = {} # use dictionary to fast check the existence
        for vertex_idx in vertices.values():
            unvisited[vertex_idx] = True
        
        stack = []
        stack.append(unvisited.keys()[0])
        num_islands = 1
        
        while True:
            vertex_idx = stack.pop()            
            if vertex_idx in unvisited:
                del unvisited[vertex_idx]
            neighbor_vertices = edges[vertex_idx]
            for neighbor_vertex in neighbor_vertices:
                if neighbor_vertex in unvisited:
                    stack.append(neighbor_vertex)
            
            if len(stack) == 0:
                if len(unvisited) > 0:
                    stack.append(unvisited.keys()[0])
                    num_islands += 1
                else:
                    break
        
        return num_islands
        
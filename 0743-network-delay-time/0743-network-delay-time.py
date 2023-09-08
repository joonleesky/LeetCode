class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        import heapq
        
        # initialization
        graph = {}
        distance = {}
        for node_idx in range(n):
            graph[node_idx+1] = {}
            distance[node_idx+1] = float('inf')
        
        for (src, trg, time) in times:
            graph[src][trg] = time
        
        # traverse with dijkstra
        heap = []
        heapq.heappush(heap, (0, k)) # (priority, item)
        distance[k] = 0
        
        while len(heap) > 0:
            cur_dist, cur_node = heapq.heappop(heap)     
            cur_edges = graph[cur_node]
            for next_node, next_dist in cur_edges.items():
                new_dist = cur_dist + next_dist
                if new_dist < distance[next_node]:
                    distance[next_node] = new_dist
                    heapq.heappush(heap, (new_dist, next_node))
        
        all_signal_dist = max(list(distance.values()))
        if all_signal_dist == float('inf'):
            return -1
        else:
            return all_signal_dist
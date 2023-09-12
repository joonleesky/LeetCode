class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """        
        # construct graph
        graph, total_price = {}, {}
        for node in range(n):
            graph[node] = {}
            total_price[node] = {}
            for stop in range(k+2):
                total_price[node][stop] = float('inf')
                    
        for flight in flights:
            source, dest, price = flight
            graph[source][dest] = price
        
        import heapq
        heap = []
        heapq.heappush(heap, (0, 0, src)) # price, stop, dst
        
        # Dijkstra
        while (len(heap) > 0):
            cur_price, num_stop, cur_node = heapq.heappop(heap)
            if num_stop > k:
                continue
            
            destinations = graph[cur_node]
            for destination, price in destinations.items():
                new_price = cur_price + price
                new_stop = num_stop + 1
                if new_price < total_price[destination][new_stop]:
                    total_price[destination][new_stop] = new_price
                    heapq.heappush(heap, (new_price, new_stop, destination))
        
        cheapest_price = min(total_price[dst].values())
        if cheapest_price == float('inf'):
            return -1
        else:
            return cheapest_price
        
        
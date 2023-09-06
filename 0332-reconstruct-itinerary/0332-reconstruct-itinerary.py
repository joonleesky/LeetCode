class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        #############################
        # construct directed graph
        vertices = []
        edges = collections.defaultdict(list)
        for ticket in tickets:
            departure = ticket[0]
            arrival = ticket[1]
            
            if departure not in vertices:
                vertices.append(departure)

            if arrival not in vertices:
                vertices.append(arrival)
                
            edges[departure].append(arrival)
                
        # sort in lexical order
        vertices = list(sorted(vertices))
        _edges = {}
        for airport, connected_airports in edges.items():
            _edges[airport] = list(sorted(connected_airports, reverse=True))
        edges = _edges
        
           #################################        
        # perform dfs in lexical order
        # if itinerary is found just return it
        stack = []
        stack.append(['JFK'])

        # there exist at least one valid itinerary
        while True:
            itinerary = stack.pop()
            if len(itinerary) == (len(tickets) + 1):
                return itinerary        
            
            cur_airport = itinerary[-1]
            if cur_airport in edges:
                connected_airports = list(edges[cur_airport])   
                
                # get remaining airports
                for idx in range(len(itinerary) -1):
                    departure = itinerary[idx]
                    arrival = itinerary[idx+1]
                    
                    if departure == cur_airport:
                        connected_airports.remove(arrival)

                for connected_airport in connected_airports:
                    new_itinerary = list(itinerary) # copy
                    new_itinerary = new_itinerary + [connected_airport]
                    stack.append(new_itinerary)
                
class airport:
    def __init__(self, flights,pv) -> None:
        self.flights = flights
        self.pv = pv
        self.visit = 1e7

    def minDistance(self, dist, Visited):
        #entirely depricated, I just liked the code
        min = 1e7
        for i in range(len(self.flights)):
            if (dist[i].distance) < min and Visited[i] == False:
                min = dist[i].distance
                min_index = i
        return min_index
    
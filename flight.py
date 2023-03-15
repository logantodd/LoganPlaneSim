class flight:
    def __init__(self, distance, price, location, destination,departure,arival) -> None:
        self.distance = distance
        self.price = price
        self.location = location
        self.destination = destination
        self.departure = departure
        self.arival = arival
        
    def __str__(self) -> str:
        return(str(self.distance))

class airport:
    def __init__(self, flights,pv) -> None:
        self.flights = flights
        self.pv = pv
        self.visit = 1e7
        pass

    def minDistance(self, dist, Visited):
        #entirely depricated, I just liked the code
        min = 1e7
        for i in range(len(self.flights)):
            if (dist[i].distance) < min and Visited[i] == False:
                min = dist[i].distance
                min_index = i
        return min_index
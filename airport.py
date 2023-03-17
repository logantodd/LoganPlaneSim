class airport:
    def __init__(self, flights, pv, name) -> None:
        self.flights = flights
        self.pv = pv
        self.name = name
        self.visit = 1e7
    
    def __str__(self) -> str:
        return(str(self.name))
    
    def __eq__(self,other):

        return(self)
    
    def __eq__(self,other):
        if self.name==other.name:

            return True
        return False
    def __ne__(self,other):
        return(self)
    def __lt__(self,other):
        return(self)
    def	__le__(self,other):
        return(self)
    def __gt__(self,other):
        return(self)
    def __ge__(self,other):
        return(self)
    def __hash__(self):
        return(hash(self.name))


    def minDistance(self, dist, Visited):
        #entirely depricated, I just liked the code
        min = 1e7
        for i in range(len(self.flights)):
            if (dist[i].distance) < min and Visited[i] == False:
                min = dist[i].distance
                min_index = i
        return min_index
    
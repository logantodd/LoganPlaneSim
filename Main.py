#This is where I will be learning Djcisdfes algortim 
import heapq

class flight:
    def __init__(self, distance, price, location, destination,departure,arival) -> None:
        self.distance = distance
        self.price = price
        self.location = location
        self.destination = destination
        self.departure = departure
        self.arival = arival
        
        pass
    
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
    
def Dijkstra(source,target):
    #goal is to find the shortest distance from source to target 
    #should return distance and path, currently only returns distance

    miniHeap=[(0,source)]
    testHeap=[(0,source)]
    visit = set()
    source.previousflights=[]
    returnlist=[]
    while miniHeap:
        p1, l1 = heapq.heappop(miniHeap)
        if l1 in visit:
            continue
        visit.add(l1)

        for i in range(len(l1.flights)):
            
            miniHeap.append((l1.flights[i].distance+p1,l1.flights[i].destination))
            
            if(l1)==target:
                returnlist.append((p1))

            miniHeap.sort()
            print(miniHeap)

    return(returnlist,)

#airport definition
KPIT = airport([],[])
KJFK = airport([],[])
KUNV = airport([],[])
KLAX = airport([],[])
EGLL = airport([],[])
airportlist=[KPIT,KJFK,KUNV,KLAX,EGLL]

#flight definition
KpitEgll = flight(1000,20,KPIT,EGLL,None,None)
KpitKlax = flight(400,20,KPIT,KLAX,None,None)
KpitKjfk = flight(500,20,KPIT,KJFK,None,None)
EgllKlax = flight(100,20,EGLL,KLAX,None,None)
EgllKjfk = flight(150,20,EGLL,KJFK,None,None)
EgllKunv = flight(1000,20,EGLL,KUNV,None,None)
KjfkKunv = flight(399,20,KJFK,KUNV,None,None)
KlaxKunv = flight(500,20,KLAX,KUNV,None,None)
KunvKunv = flight(1,20,KUNV,KUNV,None,None)
#set flights to cities
KPIT.flights=[KpitEgll,KpitKjfk,KpitKlax]
EGLL.flights=[EgllKjfk,EgllKlax,EgllKunv]
KJFK.flights=[KjfkKunv]
KLAX.flights=[KlaxKunv]
KUNV.flights=[KunvKunv]

print(Dijkstra(EGLL,KLAX))

#testflight = flight(120,20,KPIT,None, None)


#KPIT.flights.append(testflight)




#def dijkstra(graph, source):
#   for i in graph.verticies:
#        dist[i]
#        prev[i]
#        Q+=i
#    while Q != "":
#        remove u from Q 


    



#Location

#Time

#People
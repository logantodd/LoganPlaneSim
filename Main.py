#This is where I will be learning Djcisdfes algortim 
import heapq
import flight
import airport
import DataRetreval

def main(airportfile,flightfile):
    airportlist = DataRetreval.createAirports(airportfile)
    flightlist = DataRetreval.createFlights(flightfile,airportlist)
    DataRetreval.setFlightsToAirports(flightlist,airportlist)
    print(Dijkstra(airportlist[0],airportlist[6]))
    print("worked")
    pass

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


main("/Users/logantodd/Documents/GitHub/LoganPlaneSim/AirportList.csv","/Users/logantodd/Documents/GitHub/LoganPlaneSim/FlightList.csv")
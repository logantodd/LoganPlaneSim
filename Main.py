#This is where I will be learning Djcisdfes algortim 
import heapq
#import flight
import airport
import DataRetreval

def main(airportfile,flightfile):
    airportlist = DataRetreval.createAirports(airportfile)
    flightlist = DataRetreval.createFlights(flightfile,airportlist)
    DataRetreval.setFlightsToAirports(flightlist,airportlist)
    array2=(Dijkstra(airportlist[3],airportlist[2]))
    print(array2[0][0])
    print(backpath([],array2[1]))
    print("worked")
    pass

def Dijkstra(source,target):
    #goal is to find the shortest distance from source to target 
    #should return distance and path, currently only returns distance MIT Dijkstra's Algorithm

    miniHeap=[(0,source)]
#    testHeap=[(0,source)]
    visit = set()
#    source.previousflights=[]
    returnlist=[]
    while miniHeap:
        p1, l1 = heapq.heappop(miniHeap)
        if l1 in visit:
            continue
        visit.add(l1)

        for i in range(len(l1.flights)):
            print(l1.flights[i].distance)
            l1.flights[i].destination.pv.append(l1)
            miniHeap.append((int(l1.flights[i].distance)+p1,l1.flights[i].destination))
            
            if(l1)==target:
                
                returnlist.append((p1))
                print(l1.name)

            miniHeap.sort()
    print(target)
    print(target.name)
    print(target.pv)
    return([returnlist,target])

def backpath(array,airport):
    while airport.pv and airport.pv[0].name not in array:
        temp=airport.pv[0]
        array.append(temp.name)
        airport.pv=[]
        backpath(array,temp)

    return(array)




main("/Users/logantodd/Documents/GitHub/LoganPlaneSim/AirportList.csv","/Users/logantodd/Documents/GitHub/LoganPlaneSim/Test2.csv")
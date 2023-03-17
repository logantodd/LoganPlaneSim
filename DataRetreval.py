import airport
import flight

def createFlights(filename,airports):
    my_file = open(filename, "r")
    flightlist=[]
    for i in range(3000000):
        line=my_file.readline()
        if line=="":
            break
        parts=line.split(",")
        parts[0] = flight.flight((parts[1]),(parts[2]),airports[int(parts[3])],airports[int(parts[4])],parts[5],parts[6])
        flightlist.append(parts[0])
    return(flightlist)

def createAirports(filename):
    my_file = open(filename, "r")
    airportlist=[]
    for i in range(3000000):
        line=my_file.readline()
        if line=="":
            break
        parts=line.split(",")
        parts[0] = airport.airport([],[],parts[0])
        airportlist.append(parts[0])
    
    return(airportlist)

def setFlightsToAirports(Flights,Airports):
    for i in Airports:
        for y in Flights:
            if i == y.location:
                i.flights.append(y)
    


testports = createAirports("/Users/logantodd/Documents/GitHub/LoganPlaneSim/AirportList.csv")

testfly=createFlights("/Users/logantodd/Documents/GitHub/LoganPlaneSim/FlightList.csv",testports)

setFlightsToAirports(testfly,testports)
print(testports[0].flights)

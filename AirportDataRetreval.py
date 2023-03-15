import airport

def main():
    fname = "/Users/logantodd/Documents/GitHub/LoganPlaneSim/AirportList.csv"
    my_file = open(fname, "r")
    while my_file.readline == True:
        line=my_file.readline()
        parts=line.split(",")

        print(parts)
    
    #my_file.write("hello, world!\r\n")
    my_file.close()




def createAirports(filename):
    my_file = open(filename, "r")
    airportlist=[]
    for i in range(30):
        line=my_file.readline()
        if line=="":
            break
        parts=line.split(",")
        parts[0] = airport.airport(parts[1],[])
        airportlist.append(parts[0])
    
    return(airportlist)

print(createAirports("/Users/logantodd/Documents/GitHub/LoganPlaneSim/AirportList.csv"))
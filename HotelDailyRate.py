nights = 0
def hotel_cost(nights):
    x = 140 * nights
    print x
    return x

hotel_cost(5)

city = ""
rndTrp = 0
def plane_ride_cost(city):
    if city == "Charlotte":
        rndTrp = 183.00
        print "Round trip price to Charlotte: {0}".format(rndTrp)
        return rndTrp
    elif city == "Tampa":
        rndTrp = 220.00
        print "Round trip price to Tampa: {0}".format(rndTrp)
        return rndTrp
    elif city == "Pittsburgh":
        rndTrp = 222.00
        print "Round trip price to Pittsburgh: {0}".format(rndTrp)
        return rndTrp
    elif city == "Los Angeles":
        rndTrp = 475.00
        print "Round trip price to Los Angeles: {0}".format(rndTrp)
        return rndTrp

plane_ride_cost("Charlotte")    
plane_ride_cost("Tampa")
plane_ride_cost("Pittsburgh")
plane_ride_cost("Los Angeles")

days = 0
def rental_car_cost(days):
    cost = days * 40.00
    if days >= 7:
        cost -= 50.00
        print "Rental car price is: {0}".format(cost)
        return cost
    elif days >=3 and days < 7:
        cost -= 20.00
        print "Rental car price is: {0}".format(cost)
        return cost
    elif days < 3:
        cost = days * 40.00
        print "Rental car price is: {0}".format(cost)
        return cost

rental_car_cost(1)    
rental_car_cost(4)     
rental_car_cost(10) 

def trip_cost(city, days):
    totalCost = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)
    print "Total trip price is: {0}".format(totalCost)
    return totalCost

trip_cost("Charlotte", 10)

    



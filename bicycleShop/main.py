#!/usr/bin/python -tt

import random
from bicycle2 import Bicycle, BikeShop, Customer

bikes = [
    Bicycle("All Terrain", 75, 100), 
    Bicycle("Youth Jumper", 70, 150),
    Bicycle("Speed Demon", 50, 250),
    Bicycle("US MountainBike", 90, 350),
    Bicycle("Roadster", 65, 100),
    Bicycle("All Seasons", 75, 550)
]

shop = BikeShop("Tahoe Bikes", 20, bikes)

print "\nTahoe Bikes :$({} profit):".format(shop.profits())
print "-" * 20
def print_inventory(bikes):
   print "Inventory"
   print "-" * 20
   for bike in bikes:
       print "model:{} cost:{} price {}".format(bike.model, bike.cost, bike.price)

print_inventory(bikes)


customers = [
    Customer("Larry", 200),
    Customer("Bill", 500),
    Customer("Steve", 1000)
]

def print_customers(customers):
     print "\nCustomers of this bicycle store :"
     print '-' * 30
     for cust in customers:
         print "name:{} cash:{}".format(cust.name,cust.fund)
print_customers(customers)

print "\nCustomers purchased the following :"
print '-' * 35
for customer in customers:
    list_of_bikes = shop.affordable(customer)
    my_bike = random.choice(list_of_bikes)
    shop.sell_this_bike(customer, my_bike)
    print "{0} bought the {1} at ${2}. ${3} is left over.".format(customer.name, customer.bike.model, customer.bike.price, customer.fund)
   
print "\nTahoe Bikes :$({0} profit):".format(shop.profits())
print '-' * 26
print "Cycles leftover :"
print '-' * 26
available_bikes = shop.available_bikes()
for bike in available_bikes:
    print bike.model
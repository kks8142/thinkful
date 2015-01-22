class Bicycle:

    def __init__(self, model, weight, cost):

        self.model = model
        self.weight = weight
        self.cost = cost

class BikeShop:

    def __init__(self, name, margin, bikes):

        self.name = name
        self.margin = margin
        self.profit = 0
        self.inventory = {}

        for bike in bikes:

            bike.markup = int((bike.cost / 100.0) * self.margin)
            bike.price = bike.cost + bike.markup
            self.inventory[bike.model] = bike
     
    def affordable(self, customer):
        affordables = []
        bikes = self.inventory.values() 
        for bike in bikes: 
            if (bike.price <= customer.fund):
                #print "+{} {} {} ".format(bike.model, bike.price, customer.name)
                affordables.append(bike)
        return affordables

    def sell_this_bike(self, customer, bike):
        customer.bike = bike
        customer.fund -= bike.price
        self.profit += bike.markup
        #print "--{} ".format(bike.model)
        del self.inventory[bike.model]
    
    def available_bikes(self):
        return self.inventory.values()
        
    def profits(self):
        return self.profit

class Customer:
     def __init__(self, name, fund):
         self.name = name
         self.fund = fund
         self.bike = None
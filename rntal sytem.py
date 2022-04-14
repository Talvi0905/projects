#vehicle rent SYSTEM

class cycleshop:
    #def __init__(self,stock):
        #self.stock=stock
    def displycycle(self):
        print("Total cycle ",self.cycle)
    def rentforcycle(self,qty):
        if qty<=0:
            print("Enter the positive value (greter then zero)")
        elif qty>=self.cycle:
            print("Enter the value (less then stock)")
        else:
           print("Total prices",qty*100)
           print("Total cycle",self.cycle-request)
class bikeshop:
    #def __init__(self,stock):
        #self.stock=stock
    def displybike(self):
        print("Total bike",self.bike)
    def rentforbike(self,qty):
        if qty<=0:
            print("Enter the positive value (greter then zero)")
        elif qty>=self.bike:
            print("Enter the value (less then stock)")
        else:
           print("Total prices",qty*200)
           print("Total bike",self.bike-request)
class carshop(cycleshop,bikeshop):
    #def __init__(self,stock):
        #self.stock=stock
    def displycar(self):
        print("Total car",self.car)
    def rentforcar(self,qty):
        if qty<=0:
            print("Enter the positive value (greter then zero)")
        elif qty>=self.car:
            print("Enter the value (less then stock)")
        else:
           print("Total prices",qty*300)
           print("Total car",self.car-request)
class stock(carshop):
    def __init__(self,cycle,bike,car):
        self.cycle = cycle
        self.bike = bike
        self.car = car

           
while True:
    obj=stock(100,80,50)
    uc=int(input("""
            1. Disply Stock
            2. Rent for vehicle
            3. Exit
            -- """))
    if uc==1:
        obj.displycycle()
        obj.displybike()
        obj.displycar()
    elif uc==2:
        vehicle=int(input("""
                    1.cycle
                    2.bike
                    3.car
                    -- """))
        request=int(input("Enter the qty--  "))
        if vehicle==1:
            obj.rentforcycle(request)
        elif vehicle==2:
            obj.rentforbike(request)
        elif vehicle==3:
            obj.rentforcar(request)
    else:
        break
        
    

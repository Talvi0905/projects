#CYCLE RENTAL SYSTEM

class cycleshop:
    def __init__(self,stock):
        self.stock=stock
    def displycycle(self):
        print("Total cycle ",self.stock)
    def rentforcycle(self,qty):
        if qty<=0:
            print("Enter the positive value (greter then zero)")
        elif qty>=self.stock:
            print("Enter the value (less then stock)")
        else:
           print("Total prices",qty*100)
           print("Total cycle",self.stock-request)
while True:
    obj=cycleshop(100)
    uc=int(input("""
            1. Disply Stock
            2. Rent for Cycle
            3. Exit
            -- """))
    if uc==1:
        obj.displycycle()
    elif uc==2:
        request=int(input("Enter the qty--  "))
        obj.rentforcycle(request)
    else:
        break
        
    

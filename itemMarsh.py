"""
File: itemMarsh.py
""" 

class Item:
    """This will make a item that takes in name, quantity, and price"""

    def __init__(self, name, quantity, price):
        """Sets vals for name, quantity, and price"""
        self.myName = name
        self.myQuantity = quantity
        self.myPrice = price

    def setName(self, newName):
        """sets the new name"""
        self.myName = newName

        return

    def getName(self):
        """Returns the name"""
        return self.myName

    def setQuantity(self, newQuantity):
        """sets the new quantity"""
        self.myQuantity = newQuantity

        return

    def getQuantity(self):
        """Returns the quantity"""
        return self.myQuantity

    def setPrice(self, newPrice):
        """sets the new price"""
        self.myPrice = newPrice

        return

    def getPrice(self):
        """Returns the price"""
        return self.myPrice

    def __str__(self):
        """Prints out name then quantity then price all on diffrent lines"""
        ans = "Name: "+self.myName + "\n"
        ans += "Quantity: "+str(self.myQuantity) + "\n"
        ans += "Price: ${0:0.2f}".format(self.myPrice) + "\n"
        return(ans)


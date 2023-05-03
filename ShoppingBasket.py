class Item:
  # Constructor
  def __init__(self,name,price,totalquantity):
    self.name = name
    self.price = price
    self.totalquantity=totalquantity

class FruitsNVegetables(Item) :
  category="Fruits and Vegetables"
  def __init__(self,name,price,totalquantity):
    Item.__init__(self,name,price,totalquantity)
    self._GST=.20 
          
class Dairy(Item):
  category = "Dairy"
  def __init__(self,name,price,totalquantity,expiredby):
    Item.__init__(self,name,price,totalquantity)
    self.expiredby=expiredby
    self._GST=.10   
     
class Meat(Item):
  category = "Meat"
  def __init__(self,name,price,totalquantity, weight):
    Item.__init__(self,name,price,totalquantity)
    self.weight=weight
    self._GST=.18
   
class Canned(Item):
  category = "Canned"
  def __init__(self,name,price,totalquantity,brand, volume):
    Item.__init__(self,name,price,totalquantity)
    self.brand=brand
    self.volume=volume
    self._GST=.15
  
class sauces(Item):
  category = "Sauces"
  def __init__(self,name,price,totalquantity,brand, units):
    Item.__init__(self,name,price,totalquantity)
    self.brand=brand
    self.units=units
    self._GST=.12
     
     



    
class ShoppingBasket:
  # Constructor
  def __init__(self):
    self.items = {} #A dictionary of all the items in the shopping basket: {item:quantity} 
    self.checkout = False
  
  # A method to add an item to the shopping basket  
  def addItem(self,item,quantity=1):
    if quantity > 0 and quantity <= item.totalquantity: 
      #Check if the item is already in the shopping basket
      if item in self.items:
        self.items[item]= self.items[item] + quantity
      else: 
        self.items[item] = quantity
      item.totalquantity=item.totalquantity-quantity  
    else:
      print("available stock:"+str(item.totalquantity))
      
  # A method to remove an item from the shopping basket (or reduce it's quantity)  
  def removeItem(self,item):
      #Remove the item
      item.totalquantity=item.totalquantity + self.items.pop(item, None)
                            
  # A method to update the quantity of an item from the shopping basket  
  def updateItem(self,item,quantity):
    if quantity > 0: 
      item.totalquantity= item.totalquantity + (self.items[item] - quantity) 
      self.items[item] = quantity 
    else:
       if item in self.items:
        if quantity<self.items[item]:
          #Reduce the required quantity for this item
          self.items[item]= self.items[item] - quantity
          item.totalquantity=item.totalquantity + quantity
        else:
          #Remove the item
          self.items.pop(item, None)
          print("quantity to be removed exceeded, put proper qty")
  
  # A method to view/list the content of the basket.
  def view(self):
    totalCost,afterGSTcost = 0, 0
    AfterGST={}
    print("--------------------------------------------------------------------------------------------")
    for item in self.items:
      quantity = self.items[item]
      cost = quantity * item.price
      if item._GST in AfterGST:    
        AfterGST[item._GST]= AfterGST[item._GST] + item._GST * cost 
      else:
        AfterGST[item._GST]=item._GST * cost        
      print(" + " + item.category + ":\t"+item.name + " | " + str(quantity) + " x Rs" + '{0:.2f}'.format(item.price) + "\t\t\t\t = Rs" + '{0:.2f}'.format(cost))
      totalCost += cost
    print("Total(BEFORE GST)\t\t\t\t\t\t\t = Rs"+ '{0:.2f}'.format(totalCost))
    print("--------------------------------------------------------------------------------------------")  
    for i,j in AfterGST.items():
        print("GST @{}\t\t\t\t\t\t\t\t\t= Rs".format(str(i))+ str(int(j))) 
        afterGSTcost= afterGSTcost+ int(j)
    totalCost+= afterGSTcost 
    print("Total(AFTER GST)\t\t\t\t\t\t\t= Rs" + '{0:.2f}'.format(totalCost))
    print("--------------------------------------------------------------------------------------------")  
  
  # A method to empty the content of the basket
  def clearbasket(self):
    self.items = {}
    
  # A method to return whether the basket is empty or not:
  def isEmpty(self):
    return len(self.items)==0
    
  
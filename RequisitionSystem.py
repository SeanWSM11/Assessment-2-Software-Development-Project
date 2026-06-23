counter = 0

class reqSystem:
    def __init__(self, date, staffID, name):
        global counter

        self.date = date
        self.staffID = staffID
        self.name = name

        counter += 1
        self.req_id = 1000 + counter

        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_ref = None

# ADD A REQUISITION 
    def add_requisition(self):

     while True:
      items = input("Item name: ")
      price = float (input("Item price ($): "))
    
      self.items.append ((items, price)) #ADDS TO END OF EVERY LIST

      answer = input("Add another item? (yes/no): ")
      if answer.lower() != "yes":
        break
     
     self.total = 0

     for items, price in self.items:
        self.total += price

     return self.total


    def approve_requisition(self):  
     if self.total <500:
      self.status = "Approved"
      self.approval_ref = self.staffID + str(self.req_id)[-3:] #STAFF ID + 3 DIG REQID

     else:
         self.status = "Pending"

         return self.status
     
counter = 0

class reqSystem:
    def __init__(self, date, staffID, name):
        global counter

        self.date = date
        self.staffID = staffID
        self.name = name

        counter += 1
        self.req_id = 10000 + counter

        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

# ADD A REQUISITION 
    def add_requisition(self):

     while True:
      items = input("Item name: ")
      price = float(input("Item price ($): "))
    
      self.items.append ((items, price)) #ADDS TO END OF EVERY LIST

      more = input("Add another item? (yes/no): ")
      if more.lower() != "yes":
        break
     
     self.total = sum(price for _, price in self.items)
     return self.total

# APPROVE REQUISITION
    def approve_requisition(self): 
      
     if self.total <500:
      self.status = "Approved"
      self.approval_ref = self.staffID + str(self.req_id)[-3:] #STAFF ID + 3 DIG REQ-ID

     else:
         self.status = "Pending"
         self.approval_ref = "Not available"
     
     #RESPOND TO REQUISITION
    def respond_requisition(self):
      print(f"\nRequisition ID: { self.req_id}")
      print(f"Current status: {self.status}")
      print(f"Total: {self.total}")

      if self.status != "Pending":
         print("This requisition is not pending")
         return
      
      answer = input("Approve or Not Approve (A/N): ")

      if answer.upper() == "A":
         self.status = "Approved"
         self.approval_ref = self.staffID + str(self.req_id)[-3:]
        
      else:
        self.status = "Not approved"
        self.approval_ref = "Not available"
      
      #DISPLAY REQUISITIONS
    def display_requisitions(self):
      print ("\n------------------")
      print ("Date: ", self.date)
      print ("Staff ID: ", self.staffID)
      print ("Staff Name: ", self.name)
      print ("Req ID: ", self.req_id)
      print ("Total: ", self.total)
      print ("Status: ", self.status)
      print ("Approval Ref:", self.approval_ref)
      print ("------------------")
    

      #DISPLAY REQUISITION STATS
    def requisition_statistics(self, requisitions_list):

      approved = 0
      pending = 0
      not_approved = 0

      for r in requisitions_list:
        

        if r.status =="Approved":
          approved +=1

        elif r.status =="Pending":
          pending +=1 

        elif r.status == "Not approved": 
            not_approved +=1  

      print("\n ---- STATS ----")
      print ("The total number of requisitions submitted: ", len(requisitions_list))
      print ("The total number of approved requisitions: ", approved)
      print ("The total number of pending requisitions: ", pending)
      print ("The total number of not approved requisitions ", not_approved)

      return requisitions_list, approved, pending, not_approved 
    

      #TEST REQUISITION 

requisitions_list=[] #Stores my reqs
# S1
print("\n ---- Requisitions ----")
r1 = reqSystem("01/12/2026", "FN18", "Bob")
r1.items =[("Mouse", 50), ("Pen", 10)]
r1.total = sum (price for _, price in r1.items) 
r1.approve_requisition()
requisitions_list.append(r1)

# S2
r2 = reqSystem("27/03/2026", "FN17", "John")
r2.items =[("Notepad", 50), ("Laptop", 450)]
r2.total = sum (price for _, price in r2.items) 
r2.approve_requisition()
requisitions_list.append(r2)

# S3
r3 = reqSystem("21/02/2025", "FN11", "Karen")
r3.items =[("Chair", 90)]
r3.total = sum (price for _, price in r3.items) 
r3.approve_requisition()
requisitions_list.append(r3)

# S4
r4 = reqSystem("11/11/2025", "FN010", "James")
r4.items =[("Headset", 599)]
r4.total = sum (price for _, price in r4.items) 
r4.approve_requisition()
requisitions_list.append(r4)

# S5
r5 = reqSystem("31/10/2024", "FN09", "James")
r5.items =[("Desk", 222)]
r5.total = sum (price for _, price in r5.items) 
r5.approve_requisition()
requisitions_list.append(r5)

# DISPLAYS ALL
for r in requisitions_list:
    r.display_requisitions()

#STATS BEFORE MANAGER
print("\n ---- Requisition Stats ----")
r1.requisition_statistics(requisitions_list)

# PENDING RESPONSE
print("\n ---- Pending Requisitions ----")
for r in requisitions_list:
  if r.status == "Pending":
    r.respond_requisition()

#FINAL DISPLAY
print("\n ---- Final Requisitions ----")
for r in requisitions_list:
  r.display_requisitions()
app=[]
run=True
apps=4

class Application():
    group="" 
    type=""
    pay="0-100"
    def __init__(self):
        print(" You have "+str(apps)+" applications to change.")
    def details(self):
        self.group= input("enter the group name-")
        self.type= input("input the type of job-")
        self.pay= input("input the pay-")
while run:
    if apps==0:
        print("you have no applications!")
        break
    elif apps>0:
        print("add information to these apps")
        for i in range(4):
            a1= Application()
            app.append(a1)
            a1.details()
            apps-=1
        break


         
        
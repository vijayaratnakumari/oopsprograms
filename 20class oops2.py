class StudentDetials:
    def __init__(self, sid, sname, saddress):
        self.sid =sid
        self.sname=sname
        self.saddress= saddress
    def display(self):
        print("student id is:", self.sid)
        print("stident name is:", self.sname)
        print("student address is:", self.saddress)

s1=StudentDetials(101,"ratna", "mulapalem")
s1.display()
s2=StudentDetials(102, "vijaya", "bapatla")
s2.display()


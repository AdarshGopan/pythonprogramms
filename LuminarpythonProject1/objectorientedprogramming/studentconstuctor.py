class Student:
    dept="cse"
    def __init__(self,name,roll,colg_name):
        self.name=name
        self.roll_no=roll
        self.colg=colg_name
    def put(self):
        print("name = ",self.name)
        print("roll no = ",self.roll_no)
        print("college name = ",self.colg)
        print("departent name = ",Student.dept)
s1=Student("adarsh",4,"ss college poothotta")
s1.put()
class Vehicle:
    reg="kerala"
    def set(self,id):
        self.t=id
    def get(self):
        print(self.t)
class Bus(Vehicle):
    def put(self):
        print("in bus")
b=Bus()
b.set("KL 07 BK 8384")
b.get()
b.put()


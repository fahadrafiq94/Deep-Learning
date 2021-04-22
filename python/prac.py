class hello :
    name="fahad"
    def show(self):
        print(self.name)
    # def __init__(self):
    #     print("hello")
class hy(hello):
    
    def show(self):
        print(self.name)
    # def __init__(self):
    #     print("hy")
class bye(hy):

    def show(self):
        print(self.name)
    # def __init__(self):
    #     super().__init__()
    #     print("bye")
    
o = bye()
o.show()


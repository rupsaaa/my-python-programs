class Base:
    def show(self):
        print("This is codeHUB sodepur")
class Child(Base):
    def show(self):#overriding show() function
        super().show()#Parent class show()
        print("A computer programming centre")
c=Child()
c.show()#Child class show()



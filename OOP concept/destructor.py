class Test:
    def __init__(self,nm):
        self.nm=nm
        print(f"object {self.nm} is created")
    def __del__(self):
        print(f"object {self.nm} is destroyed")
ob1=Test("Debrup")
ob2=Test("Rupsa")
del ob1 #manually destroying the object
print("end...")#object getting destroyed automatically after the end of program(GC/garbage collection )

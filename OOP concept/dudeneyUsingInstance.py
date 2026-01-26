class Dudeney:
    def __init__(self,s,e):
        self.start=s
        self.end=e
    def isDudeney(self,n):
        n1=n
        s=0
        while(n!=0):
            s=s+(n%10)
            n=n//10
        if(s**3==n1):
            return 1
    def display(self):
        for i in range(self.start,self.end+1):
            if(self.isDudeney(i)==1):
                print(i)
ob=Dudeney(500,20000)
ob.display()


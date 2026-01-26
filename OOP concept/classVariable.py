class Sample:
    a=5
    @classmethod
    def modify(cls):
        cls.a+=1
        
s1=Sample()
s2=Sample()
print("a in s1:",s1.a)
print("a in s2:",s2.a)
s1.modify()
print("a in s1:",s1.a)
print("a in s2:",s2.a)
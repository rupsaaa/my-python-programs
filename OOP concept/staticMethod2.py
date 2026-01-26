class find:
    @staticmethod
    def factorial(n):
        if n==0:
            return 1
        return n*find.factorial(n-1)
    @staticmethod
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
print(find.factorial(4))
print(find.gcd(35,10))


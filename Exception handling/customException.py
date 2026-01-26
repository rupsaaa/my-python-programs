class small_number_error(Exception):
    def __init__(self,divisor,message="Division is small.Its greater than 2"):
        self.divisor=divisor
        self.message=message
        super().__init__(self.message) #calling constructor of super class Exception
try:
    num=30
    divisor=int(input("Enter a divisor:"))
    if divisor<=2:
        raise small_number_error(divisor)
    result=num/divisor
    print("Result:",result)
except small_number_error as o:
    print(f"Error: {o} Divisor: {o.divisor}")
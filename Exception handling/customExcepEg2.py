class StringLongError(Exception):
    def __init__(self,length,limit=9):
        self.length=length
        self.limit=limit
        super().__init__(f"String length({self.length}) cross the limit ({self.limit})")
try:
    text=input("Enter a string (max 9 chars):")
    if len(text)>9:
        raise StringLongError(len(text))
    print(f"valid input:{text}")
except StringLongError as e:
    print(f"Error:{e}")   
    
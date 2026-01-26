class check_pal:
    def check(self,val=None):
        if val is None:
            print ("no input is present")
        else:
            value=str(val)
            if value==value[::-1]:
                print(f"{val} is palindrome")
            else:
                print(f"{val} is not palindrome")
ob=check_pal()
num=131
string="Rupsa"
ob.check(num)
ob.check(string)
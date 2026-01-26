lt1=[]
lt2=[]
n1=int(input("Enter size of first list:"))
print("Enter the elements of first list:")
for i in range(n1):
    num=int(input())
    lt1.append(num)
n2=int(input("Enter size of second list:"))
print("Enter the elements of first list:")
for i in range(n2):
    num=int(input())
    lt2.append(num)

if len(lt1)!=len(lt2):
   exit()
else:
   a=set(lt1)-set(lt2)
   b=set(lt2)-set(lt1)
   c=list(a|b)
   if len(c)==0:
      print("The lists are identical")
   else:
      print("Difference of lists:",c)
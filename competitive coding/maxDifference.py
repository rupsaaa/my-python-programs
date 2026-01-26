#input:[7,1,5,3,6,4]  Output:5(buy at 1 sell at 6)
lt=list(map(int,input().split()))
for i in range(len(lt)):
   minno=min(lt)
   if lt[-1]==minno:
      lt.remove(minno)
      if len(lt)==0:
         print(0)
         exit()
      minno=min(lt)
   minind=lt.index(minno)
   maxno=max(lt[minind:])
print(maxno-minno)
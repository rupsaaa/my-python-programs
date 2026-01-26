N = int(input()) 
M = int(input())
c = '.|.'

for i in range(N//2):
    print((c * i).rjust(M//2-1,"-") + c + (c * i).ljust(M//2-1,"-"))
print('WELCOME'.center(M,"-"))
for i in range(N//2-1,0,-1):
    print((c * i).rjust(M//2-1,"-") + c + (c * i).ljust(M//2-1,"-"))
print((c * 0).rjust(M//2-1,"-") + c + (c * 0).ljust(M//2-1,"-"))
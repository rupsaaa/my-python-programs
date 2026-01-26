def dec_to_bin(dec):
    if(dec==0):
        print(1,end='') 
        
    else:
        dec_to_bin(dec//2)
        print(dec%2,end='')
        
print(dec_to_bin(15))
    
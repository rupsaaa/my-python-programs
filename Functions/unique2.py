def inverted(num):
    unique=[i for i in num if len(str(i))==len(set(str(i)))]
    print (unique)
t=(234,455,567,557,489)
inverted(t)

import math
def perfect_sq(num):
    if num<0:
        return False
    root=math.isqrt(num)
    return num==root*root
numbers=[4,6,16,8,9,30,36,40,49,81]
perfect_square=[num for num in numbers if perfect_sq(num)]
print("Perfect squares in the list:",perfect_square)
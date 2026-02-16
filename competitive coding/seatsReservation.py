'''Indian Railways is developing a new reservation system. Each passenger enters a preferred seat number while booking.
Due to system limitations, If a seat is already booked, the passenger is rejected.Only the first passenger gets the seat.
You are given a list of seat requests.
Write a program to find:
Number of passengers who got seats and who were rejected
INPUT: seats = [10, 20, 10, 30, 40, 20, 50] 
OUTPUT:
Booked: 5
Rejected: 2'''

from collections import Counter
seats = [10, 20, 10, 30, 40, 20, 50]
dt=Counter(seats)
lt=[k for k,v in dt.items() if v>1]
print("Booked:",len(seats)-len(lt))
print("Rejected:",len(lt))
        
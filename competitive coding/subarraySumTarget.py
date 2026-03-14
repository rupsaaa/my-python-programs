'''A bank monitors transactions to detect suspicious activity.
If a continuous sequence of transactions equals a suspicious amount, the system flags it.
Find if any subarray has sum = target.'''

transactions = [10, 15, -5, 20, 10]
target = 28
def subarray_sum_target(transactions, target):
    sum=0
    seen=set()
    for i in transactions:
        sum+=i
        if sum == target or (sum-target) in seen:
            return True
        seen.add(sum)
    return False
print(subarray_sum_target(transactions, target))
    
    
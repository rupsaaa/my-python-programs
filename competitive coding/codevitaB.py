balance=int(input())
n=int(input())
transactions=[]
committed=[]
readval=[]
c=0
for i in range(n):
    parts=input().split()
    op=parts[0]
    if op=="read":
        readval.append(balance)
    elif op=="credit":
        amount=int(parts[1])
        balance+=amount
        transactions.append(("credit", amount))
        c+=1
    elif op=="debit":
        amount=int(parts[1])
        balance-=amount
        transactions.append(("debit", amount))
        c+=1
    elif op=="abort":
        x=int(parts[1])
        cc=committed[-1][1] if committed else 0
        if x>cc:
            idx=x-cc-1
            if idx>=0 and idx<len(transactions):
                t_type,amount=transactions[idx]
                if t_type=="credit":
                    balance-=amount
                elif t_type=="debit":
                    balance+=amount
                transactions[idx] = ("aborted",0)
    elif op=="rollback":
        x=int(parts[1])
        if x>=1 and x<=len(committed):
            balance=committed[x-1][0]
            transactions.clear()
            c=committed[x-1][1]
    elif op=="commit":
        committed.append((balance,c))
        transactions.clear()  
for i in readval:
    print(i)
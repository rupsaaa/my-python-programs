import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Sample Transactional Data
transactions = [
    ['milk', 'bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'eggs'],
    ['bread', 'butter'],
    ['bread', 'eggs']
]

# 1. Prepare the data for Apriori
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 2. Find Frequent Itemsets using Apriori
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# 3. Generate Association Rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)

print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

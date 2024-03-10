import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def apply_apriori(transactions, min_support, min_confidence):
    # Convert list of transactions to DataFrame and apply one-hot encoding
    one_hot_encoded = pd.get_dummies(pd.DataFrame(transactions).stack()).groupby(level=0).sum()
    one_hot_encoded = one_hot_encoded.astype(bool)
    
    frequent_itemsets = apriori(one_hot_encoded, min_support=min_support, use_colnames=True)
    
    if frequent_itemsets.empty:
        print("No frequent itemsets found with the specified minimum support threshold.")
        return None, None
    
    association_rules_df = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    
    # Convert confidence and support values to formatted strings with "%" symbol
    association_rules_df['confidence'] = association_rules_df['confidence'].apply(lambda x: '{:.2f}%'.format(x * 100))
    association_rules_df['support'] = association_rules_df['support'].apply(lambda x: '{:.2f}%'.format(x * 100))
    
    if association_rules_df.empty:
        return frequent_itemsets, None
    
    return frequent_itemsets, association_rules_df

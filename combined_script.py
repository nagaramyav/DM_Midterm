from file_input import select_database, read_transactions_from_file
from apriori_algorithm import apply_apriori
from fp_growth_algorithm import apply_fp_growth
from brute_force_algorithm import find_association_rules

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
import time

# Read transactions from file
selected_database = select_database()
if selected_database:
    # Read the selected database
    dataset = pd.read_csv(selected_database)

    # Preprocess the dataset
    transactions = [transaction.split(',') for transaction in dataset['Transactions']]
    #print("Input Transactions:")
    #print(transactions)
    te = TransactionEncoder()
    te_ary = te.fit_transform(transactions)
    dataSet = pd.DataFrame(te_ary, columns=te.columns_)

    # Prompt user to enter support and confidence thresholds as percentages
    min_support_percentage = float(input("Enter the minimum support threshold (percentage): "))
    min_confidence_percentage = float(input("Enter the minimum confidence threshold (percentage): "))

    # Convert percentage thresholds to proportions
    min_support = min_support_percentage / 100
    min_confidence = min_confidence_percentage / 100

    #print(f"Minimum Support Threshold main: {min_support_percentage}%")
    #print(f"Minimum Support Value main: {min_support}")

    min_support_count = min_support * len(transactions)
    #print(f"Minimum Support Count main: {min_support_count}")

    # Apply Apriori algorithm
    print("\n--- Apriori Algorithm ---")
    start_time = time.time()
    frequent_itemsets_apriori, association_rules_apriori = apply_apriori(transactions, min_support, min_confidence)
    end_time = time.time()
    apriori_time = end_time - start_time
    print(f"Time taken by Apriori algorithm: {apriori_time:.6f} seconds")

    if association_rules_apriori is None:
        print("There are no association rules for the min confidence provided (Apriori).")
    else:
        print("Final Association rules (Apriori):")
        for i, rule in enumerate(association_rules_apriori.iterrows(), start=1):
            antecedent = list(rule[1]['antecedents'])
            consequent = list(rule[1]['consequents'])
            confidence = rule[1]['confidence']
            support = rule[1]['support']
            print(f"Rule {i}: {antecedent} -> {consequent}")
            print(f"Confidence: {confidence}") 
            print(f"Support: {support}")


    # Apply FP-Growth algorithm
    print("\n--- FP-Growth Algorithm ---")
    start_time = time.time()
    frequent_itemsets_fpgrowth, association_rules_fpgrowth = apply_fp_growth(transactions, min_support, min_confidence)
    end_time = time.time()
    fpgrowth_time = end_time - start_time
    print(f"Time taken by FP-Growth algorithm: {fpgrowth_time:.6f} seconds")

    if association_rules_fpgrowth is None:
        print("There are no association rules for the min confidence provided (FP-Growth).")
    else:
        print("Final Association rules (FP-Growth):")
        for i, rule in enumerate(association_rules_fpgrowth.iterrows(), start=1):
            antecedent = list(rule[1]['antecedents'])
            consequent = list(rule[1]['consequents'])
            confidence = rule[1]['confidence']
            support = rule[1]['support']
            print(f"Rule {i}: {antecedent} -> {consequent}")
            print(f"Confidence: {confidence}") 
            print(f"Support: {support}")


    # Apply Brute Force algorithm
    print("\n--- Brute Force Algorithm ---")
    start_time = time.time()
    frequent_itemsets, association_rules = find_association_rules(transactions, min_support, min_confidence)
    end_time = time.time()
    bruteforce_time = end_time - start_time
    print(f"Time taken by Brute Force algorithm: {bruteforce_time:.6f} seconds")

    if association_rules:
        print("Final Association Rules (Brute Force):")
        for i, rule in enumerate(association_rules, start=1):
            antecedent, consequent, support, confidence = rule
            print(f"Rule {i}: {antecedent} -> {consequent}")
            print(f"Confidence: {confidence :.2f}%")
            print(f"Support: {support :.2f}%")
    else:
        print("\nThere are no association rules for the min confidence provided (Brute Force).")

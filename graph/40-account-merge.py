
from disjoint_set import DisjointSet
from collections import defaultdict


def accounts(graph):
    ds = DisjointSet()
    
    for i, account_list in graph:
        ds.add(i)
        for account in account_list:
            ds.add(account)
            if ds.find(account) != account:
                ds.union(ds.find(account), i)
            else:
                ds.union(i, account)
                
    merged_account = defaultdict(list)
    
    for i in ds.parents.key():
        root = ds.find(i)
        merged_account[root].append(i)
        
        
    final_merged_account = list(merged_account.values())
    return final_merged_account
                
                
     
        
        
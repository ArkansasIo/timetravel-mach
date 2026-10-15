"""Tiny causal graph example using only the Python standard library."""
from collections import defaultdict, deque

def is_acyclic(edges):
    nodes=set()
    outgoing=defaultdict(list)
    indegree=defaultdict(int)
    for source,target in edges:
        nodes.update((source,target))
        outgoing[source].append(target)
        indegree[target]+=1
        indegree.setdefault(source,0)
    queue=deque(n for n in nodes if indegree[n]==0)
    visited=0
    while queue:
        node=queue.popleft()
        visited+=1
        for target in outgoing[node]:
            indegree[target]-=1
            if indegree[target]==0:
                queue.append(target)
    return visited==len(nodes)

if __name__ == "__main__":
    ordinary=[("A","B"),("B","C")]
    cycle=[("A","B"),("B","C"),("C","A")]
    print({"ordinary_order_acyclic":is_acyclic(ordinary),"cycle_acyclic":is_acyclic(cycle)})
    print("Graph cycles are a mathematical property, not evidence of physical time travel.")

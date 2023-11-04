import heapq

from graph.mst.DisjointSet import DisjointSet


def minimumSpanningTree(edges, n: int):
    min_heap = []
    for s, d, w in edges:
        heapq.heappush(min_heap, [w, s, d])

    dset = DisjointSet(n)
    mst = []
    while len(mst) < n - 1:
        w, s, d = heapq.heappop(min_heap)
        if not dset.union(s, d):
            continue
        mst.append([s, d])
    return mst
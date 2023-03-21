import heapq

def merge_sorter(*args):
    heap = []

    for seq_idx, seq in enumerate(args):
        try:
            it = iter(seq)
            heapq.heappush(heap, (next(it), seq_idx, it))
        except StopIteration:
            pass

    while heap:
        smallest_elem, seq_index, it = heapq.heappop(heap)
        yield smallest_elem

        try:
            heapq.heappush(heap, (next(it), seq_index, it))
        except StopIteration:
            pass
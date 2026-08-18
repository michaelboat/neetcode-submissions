class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freqs = Counter(tasks)
        maxHeap = [-val for val in freqs.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        while maxHeap:
            cycle = n+1
            store = []
            task_ct = 0

            while cycle and maxHeap:
                curr = -heapq.heappop(maxHeap)
                if curr > 1:
                    store.append(curr-1)
                task_ct += 1
                cycle -= 1
            
            for num in store:
                heapq.heappush(maxHeap, -num)
            time += task_ct if not maxHeap else n+1

        return time
        
        
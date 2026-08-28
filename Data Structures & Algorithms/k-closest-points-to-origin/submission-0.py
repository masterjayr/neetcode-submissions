class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2) # origin - 0, 0 so no need to do (x1-x2)**2 + (y2-y1)**2 since y1 is always 0
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap) # make it into a minHeap ordering by distance
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap) # get top smallest distance and reorder heap
            res.append([x,y])
            k-=1

        return res
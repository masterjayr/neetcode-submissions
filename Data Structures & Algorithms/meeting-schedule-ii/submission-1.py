"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]: # meaning a new meeting starting
                count += 1
                s += 1
            else: # meaning meeting just ended so decrement count
                count -= 1
                e += 1
            res = max(count, res) # max rooms encountered so far
        
        return res
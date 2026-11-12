"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        heap = []
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        # put end times in min heap
        for e in end_times:
            heappush(heap, e)
        
        for s in start_times:
            if s >= heap[0]:
                heappop(heap)
        
        return len(heap)

        # # 1. Extract and sort start/end times greedily from the objects
        # starts = sorted([i.start for i in intervals])
        # ends = sorted([i.end for i in intervals])

        # count, res = 0, 0

        # # iterate through start times
        # s_ptr = 0
        # e_ptr = 0

        # while s_ptr < len(intervals):
        #     if starts[s_ptr] < ends[e_ptr]:
        #         count += 1
        #         s_ptr += 1
        #     else:
        #         e_ptr += 1
        #         count -= 1
        #     res = max(res, count)
        # return res













        # start_times = sorted([i.start for i in intervals])
        # end_times = sorted([i.end for i in intervals])

        # s [0,5,15]
        # e [10,20,40]

        # s_ptr = 0
        # e_ptr = 0

        # current_rooms = 0
        # max_rooms = 0

        # # 2. Walk through all starting meetings
        # while s_ptr < len(intervals):
        #     # If a meeting starts before the oldest active one finishes
        #     if start_times[s_ptr] < end_times[e_ptr]:
        #         current_rooms += 1
        #         s_ptr += 1
        #     else:
        #         # A room freed up, reuse it
        #         current_rooms -= 1
        #         e_ptr += 1

        #     # Keep track of the peak room demand
        #     max_rooms = max(max_rooms, current_rooms)

        # return max_rooms
        
        
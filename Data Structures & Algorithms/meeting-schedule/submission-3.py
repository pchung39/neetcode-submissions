"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # iterate through meeting rooms
        #     condition: each meeting should not interfere
        #     with each other
        #     what does that mean? one's end shouldn't collide with second's start. 
        intervals.sort(key=lambda i: i.start)  
        if len(intervals) == 0:
            return True
        current = intervals[0]
        curr_start, curr_end = current.start, current.end

        for nxt in range(1,len(intervals)):
            nxt_start, nxt_end = intervals[nxt].start, intervals[nxt].end
            if curr_end > nxt_start:
                return False
            
            curr_start, curr_end = nxt_start, nxt_end

        return True

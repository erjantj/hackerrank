from heapq import heappush, heappop

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
def overlaps(slot1, slot2):
    if slot1.start <= slot2.end and slot2.start <= slot1.end:
        return True
    return False

def merge(intervals):
    if not intervals:
        return []
    
    intervals_index = []
    for i in range(len(intervals)):
        heappush(intervals_index, (intervals[i].start, intervals[i].end, intervals[i]))

    first_slot = heappop(intervals_index)
    merged_intervals = [first_slot[2]]

    merged_index = 0
    while intervals_index:
        row = heappop(intervals_index)
        interval = row[2]
        if overlaps(interval, merged_intervals[merged_index]):
            merged_intervals[merged_index] = Interval(
                min(interval.start,merged_intervals[merged_index].start),
                max(interval.end,merged_intervals[merged_index].end)
            )
        else:
            merged_intervals.append(interval)
            merged_index += 1

    return merged_intervals

intervals =  [[1,3],[2,6],[8,10],[15,18]]
intervals =  [[1,3],[2,6],[5,10],[9,18]]
intervals =  [[1,3]]
intervals =  [[1,3],[1,3]]
intervals =  [Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)]
intervals =  [Interval(2,3),Interval(2,5)]
intervals =  [Interval(2,3),Interval(2,3)]
# intervals =  [Interval(6,8), Interval(2,3),Interval(2,5)]
print(merge(intervals))
        
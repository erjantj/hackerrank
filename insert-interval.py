# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def printIntervals(intervals):
    for interval in intervals:
        print(interval.start,interval.end)

def merge(interval1, interval2):
    return Interval(min(interval1.start, interval2.start), max(interval1.end, interval2.end))

def overlaps(interval1, interval2):
    if interval1.end < interval2.start or interval2.end < interval1.start:
        return False
    return True

def insert(intervals, newInterval):
    if not newInterval and not intervals:
        return []

    if not newInterval:
        return intervals

    if not intervals:
        return [newInterval]

    merged_intervals = []
    merge_index = -1
    merged = False

    for i in range(0, len(intervals)):
        curr_interval = intervals[i]
        if not merged:
            if not overlaps(curr_interval, newInterval):
                if newInterval.end < curr_interval.start:
                    merged_intervals.append(newInterval)
                    merged_intervals.append(curr_interval)
                    merge_index += 2
                    merged = True
                else:
                    merged_intervals.append(curr_interval)
                    merge_index += 1
            else:
                merged_intervals.append(merge(curr_interval, newInterval))
                merge_index += 1
                merged = True

        else:
            if merged_intervals and overlaps(merged_intervals[merge_index], curr_interval):
                merged_intervals[merge_index] = merge(merged_intervals[merge_index], curr_interval)
            else:
                merged_intervals.append(curr_interval)
                merge_index += 1
    if not merged:
        merged_intervals.append(newInterval)
        merge_index += 1

    return merged_intervals


# intervals = [Interval(1,3),Interval(6,9)]
# newInterval = Interval(2,5)

intervals = [Interval(10,11)]
newInterval = Interval(4,8)


printIntervals(insert(intervals, newInterval))


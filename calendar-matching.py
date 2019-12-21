def toTimeString(time):
    m = time%60
    h = (time - m)//60
    if m == 0:
        return '%s:00'%(h)
    return '%s:%s'%(h,m)

def toMinutes(string):
    h, m = string.split(':')
    return int(h) * 60 + int(m)

def slotToMinute(slot):
    if slot:
        return [toMinutes(slot[0]), toMinutes(slot[1])]
    return []

def slotsInsersect(slot1, slot2):
    if (slot1[0] <= slot2[0] and slot1[1] <= slot2[0]) or (slot1[0] >= slot2[1] and slot1[1] >= slot2[1]):
        return False
    return True

def mergeSlots(slot1, slot2):
    return [min(slot1[0], slot2[0]), max(slot1[1], slot2[1])]

def getSlots(calendar1, calendar2):
    slots = []    
    i = j = 0
    while i < len(calendar1) and j < len(calendar2):
        slot1 = slotToMinute(calendar1[i])
        slot2 = slotToMinute(calendar2[j])

        if slotsInsersect(slot1, slot2):
            slots.append(mergeSlots(slot1, slot2))
            i += 1
            j += 1
        if slot1[1] <= slot2[0]:
            i += 1
            if slots and slotsInsersect(slots[-1], slot1):
                slots[-1] = mergeSlots(slots[-1], slot1)
            else:
                slots.append(slot1)
        elif slot1[0] >= slot2[1]:
            j += 1
            if slots and slotsInsersect(slots[-1], slot2):
                slots[-1] = mergeSlots(slots[-1], slot2)
            else:
                slots.append(slot2)

    if calendar1[i:]:
        slots += [slotToMinute(slot) for slot in calendar1[i:]]
    if calendar2[j:]:
        slots += [slotToMinute(slot) for slot in calendar2[j:]]
    return slots

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    ranges = []
    calendar1 = [['0:00', dailyBounds1[0]]] + calendar1 + [[dailyBounds1[1], '23:59']]
    calendar2 = [['0:00', dailyBounds2[0]]] + calendar2 + [[dailyBounds2[1], '23:59']]

    slots = getSlots(calendar1, calendar2)

    for i in range(1, len(slots)):
        if slots[i][0]-slots[i-1][1] >= meetingDuration:
            ranges.append([toTimeString(slots[i-1][1]), toTimeString(slots[i][0])])
    return ranges

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30


calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['14:30', '18:10']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['13:10', '14:20'], ['17:30', '18:00'], ['18:10', '19:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 10


# calendar1 = [['9:00', '9:30'], ['9:40', '9:55']]
# dailyBounds1 = ['9:00', '10:00']
# calendar2 = [['8:00', '9:30'], ['9:35', '10:00']]
# dailyBounds2 = ['8:00', '10:30']
# meetingDuration = 1

# calendar1 = [['9:40', '9:55']]
# dailyBounds1 = ['7:00', '10:20']
# calendar2 = [['8:00', '9:00'], ['9:35', '10:00']]
# dailyBounds2 = ['7:15', '10:30']
# meetingDuration = 5

# calendar1 = [['9:00', '9:30'], ['9:40', '9:55']]
# dailyBounds1 = ['9:20', '12:00']
# calendar2 = []
# dailyBounds2 = ['8:00', '10:30']
# meetingDuration = 10

# calendar1 = []
# dailyBounds1 = ['9:00', '10:15']
# calendar2 = []
# dailyBounds2 = ['9:10', '10:30']
# meetingDuration = 5

# calendar1 = [['9:00', '9:30'], ['9:40', '9:55']]
# dailyBounds1 = []
# calendar2 = [['8:00', '9:30'], ['9:35', '10:00']]
# dailyBounds2 = ['8:00', '10:30']
# meetingDuration = 5

# calendar1 = [['9:00', '9:30'], ['9:40', '9:55']]
# dailyBounds1 = []
# calendar2 = [['8:00', '9:30'], ['9:35', '10:00']]
# dailyBounds2 = []
# meetingDuration = 5

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))


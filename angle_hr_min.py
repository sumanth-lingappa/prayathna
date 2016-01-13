__author__ = 'Sumanth_Lingappa'


def angleHourMin(hour,minute):
    # Hour hand covers 0.5 degrees per minute
    # minute hand covers 6 degrees per  minute
    # find the angeles covered by Hour and Minute hand separately, and absolute subtraction between two, is the answer

    hourAngle = 0.5 * ((hour * 60) + minute)
    minuteAngle = 6 * minute

    return abs(hourAngle - minuteAngle)


print angleHourMin(3,30)

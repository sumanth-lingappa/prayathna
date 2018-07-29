"""
This code does not allow more than 1 instance
"""


class LimitInstances(object):
    max_object = 2
    curr_objects = 0

    def __new__(cls, *args, **kwargs):
        if cls.curr_objects >= cls.max_object:
            print 'Max objects reached. Cant create another object'
        else:
            cls.curr_objects += 1


instObj1 = LimitInstances(); print instObj1
instObj2 = LimitInstances(); print instObj2
instObj3 = LimitInstances(); print instObj3


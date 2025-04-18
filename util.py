import re

"""
12가 3456
123가 3456

https://github.com/computervisioneng/automatic-number-plate-recognition-python-yolov8/blob/main/util.py
"""
def check_lp_format(text):
    if len(text) != 8 or len(text) != 9:
        return False

    t = text.split()
    print(t)

    # p = re.compile('[ㄱ-힣]')
    # r = p.search(text)
    #
    # if r is None:
    #     return False
    # else:
    #     return True

check_lp_format("12가 3456")
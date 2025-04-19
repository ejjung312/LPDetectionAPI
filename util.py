import re

"""
12가 3456
123가 3456
"""
def check_lp_format(text):
    text_len = int(len(text))
    if text_len != 7 and text_len != 8:
        return False

    # 한글인지 확인
    p = re.compile('[ㄱ-힣]')
    r = p.search(text)
    if r is None:
        return False

    pos = r.span()[1]
    t1 = text[:pos]
    t2 = text[pos:]

    # 숫자인지 확인
    if not t1[:-1].isdecimal():
        return False
    if not t2.isdecimal():
        return False

    return True

if __name__ == "__main__":
    check_lp_format("12가3456")
def is_leap(year: int) -> bool:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else :
        return False

assert not is_leap(1800)
assert not is_leap(1999)
assert is_leap(2000)
assert is_leap(2400)
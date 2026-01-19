import random



def random_odd_number() -> int:
    num = random.randint(0, 99)
    if num % 2 == 0:
        num += 1
    return num

print(random_odd_number())
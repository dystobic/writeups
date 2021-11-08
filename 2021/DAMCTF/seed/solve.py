#/usr/bin/python3

import time
import random
import hashlib

history = [
        0.3322089622063289,
        0.10859805708337256,
        0.39751456956943265,
        0.6194981263678604,
        0.32054505821893853,
        0.2674908181379442,
        0.5379388350878211,
        0.7799698997586163,
        0.6893538761284775,
        0.7171513961367021,
        0.29362186264112344,
        0.06571100672753238,
        0.9607588522085679,
        0.33534977507836194,
        0.07384192274198853,
        0.1448081453121044
]

def seed():
    return round(time.time())

def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def main():
    for s in range(seed(), 0, -1):
        random.seed(s, version=2)

        t = s
        history_check = True

        for h in history:
            if h != random.random():
                history_check = False
                break
            else:
                print(f"matching h={h} for s={t}")
                t += 1
                random.seed(t, version=2)

        if history_check:
            flag = hash(random.random())
            assert('b9ff3ebf' in flag)
            print(f"flag=dam{{{flag}}}")
            break

if __name__ == '__main__':
    main()

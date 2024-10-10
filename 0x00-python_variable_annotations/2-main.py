#!/usr/bin/env python3

from math import floor


floor = __import__('2-floor').floor

ans = floor(3.14)
print(ans == floor(3.14))
print(ans.__annotations__)
print(f" floor(3.14)    returns {ans}, which is a {type(ans)}")